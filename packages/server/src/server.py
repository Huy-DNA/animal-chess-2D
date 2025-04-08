from typing import Dict, Tuple
from PodSixNet.Channel import Channel
from PodSixNet.Server import Server

Addr = Tuple[str, int]


class ClientChannel(Channel):
    _server: "GameServer"

    def Network(self, data):
        pass

    def handle_close(self):
        super().handle_close()
        self._server.remove_client(self.addr)


class GameServer(Server):
    channelClass = ClientChannel

    __registered_clients: Dict[Addr, ClientChannel]

    def __init__(self, *, ip: str, port: int, listeners=10):
        print(f"Server listening on {ip}:{port}...")
        super().__init__(localaddr=(ip, port), listeners=listeners)
        self.__registered_clients = {}

    def Connected(self, channel: ClientChannel, addr: Addr):
        self.__registered_clients[addr] = channel

    def remove_client(self, addr: Addr):
        self.__registered_clients.pop(addr)
