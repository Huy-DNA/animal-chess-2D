import os
from time import sleep
from dotenv import load_dotenv
from core.piece import Piece, Color, PieceType
from core.map import Position
from controller.network import ServerConnector

load_dotenv()
SERVER_ADDRESS = os.getenv("SERVER_ADDRESS") or "0.0.0.0"
SERVER_PORT = int(os.getenv("SERVER_PORT") or 8686)
connector = ServerConnector(ip = SERVER_ADDRESS, port = SERVER_PORT)
connector.Send(
    {
        "action": "move",
        "piece": Piece.Schema().dump(Piece(Color.RED, PieceType.ELEPHANT)),
        "position": Position.Schema().dump(Position(1, 2)),
    },
)
connector.Send(
    {
        "action": "find_game",
    }
)
connector.Send(
    {
        "action": "start_game",
    }
)
connector.Send(
    {
        "action": "concede",
    }
)
while True:
    connector.Pump()
    sleep(0.0001)
