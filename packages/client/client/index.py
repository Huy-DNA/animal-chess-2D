import os
from time import sleep
from dotenv import load_dotenv
from PodSixNet.Connection import connection
from core.piece import Piece, Color, PieceType
from core.map import Position

load_dotenv()
SERVER_ADDRESS = os.getenv("SERVER_ADDRESS") or "0.0.0.0"
SERVER_PORT = int(os.getenv("SERVER_PORT") or 8686)
connection.DoConnect((SERVER_ADDRESS, SERVER_PORT))
connection.Send(
    {
        "action": "move",
        "piece": Piece.Schema().dump(Piece(Color.RED, PieceType.ELEPHANT)),
        "position": Position.Schema().dump(Position(1, 2)),
    },
)
while True:
    connection.Pump()
    sleep(0.0001)
