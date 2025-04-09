from re import Match
from core.piece import Piece
from core.map import Position
from typing import Dict, Tuple
from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from queue import Queue

from server.match import MatchId

Addr = Tuple[str, int]


class ClientChannel(Channel):
    _server: "GameServer"

    def Network_move(self, data):
        piece: Piece
        pos: Position
        try:
            piece = Piece.Schema().load(data["piece"])
            pos = Position.Schema().load(data["position"])
        except Exception:
            self.Send({ "action": "error", "message": "Invalid payload" })
            return

    def Network_find_game(self, data):
        pass

    def Network_start_game(self, data):
        pass

    def Network_concede(self, data):
        pass

    def handle_close(self):
        super().handle_close()
        self._server.remove_client(self.addr)


class GameServer(Server):
    channelClass = ClientChannel

    __registered_clients: Dict[Addr, ClientChannel]
    __matches: Dict[MatchId, Match]
    __client_matches: Dict[Addr, MatchId]
    __pending_clients: Queue[Addr]

    def __init__(self, *, ip: str, port: int, listeners=10):
        print(f"Server listening on {ip}:{port}...")
        super().__init__(localaddr=(ip, port), listeners=listeners)
        self.__registered_clients = {}
        self.__matches = {}
        self.__client_matches = {}
        self.__pending_clients = Queue()

    def Connected(self, channel: ClientChannel, addr: Addr):
        self.__registered_clients[addr] = channel

    def remove_client(self, addr: Addr):
        self.__registered_clients.pop(addr)
