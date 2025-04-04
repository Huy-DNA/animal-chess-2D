from typing import Dict, List, Optional
from core.map import Cell, Location, Position, DEFAULT_MAP, Map
from core.piece import Color, Piece, PieceType


class State:
    __map: Map
    __piece_positions: Dict[Piece, Optional[Position]]

    def __init__(self, map=DEFAULT_MAP):
        self.__map = map
        self.__piece_positions = {
            Piece(Color.RED, PieceType.ELEPHANT): Position(6, 2),
            Piece(Color.RED, PieceType.LION): Position(0, 0),
            Piece(Color.RED, PieceType.TIGER): Position(6, 0),
            Piece(Color.RED, PieceType.LEOPARD): Position(2, 2),
            Piece(Color.RED, PieceType.DOG): Position(1, 1),
            Piece(Color.RED, PieceType.WOLF): Position(4, 2),
            Piece(Color.RED, PieceType.CAT): Position(5, 1),
            Piece(Color.RED, PieceType.MOUSE): Position(0, 2),
            Piece(Color.BLUE, PieceType.ELEPHANT): Position(0, 6),
            Piece(Color.BLUE, PieceType.LION): Position(6, 8),
            Piece(Color.BLUE, PieceType.TIGER): Position(0, 8),
            Piece(Color.BLUE, PieceType.LEOPARD): Position(4, 6),
            Piece(Color.BLUE, PieceType.DOG): Position(5, 7),
            Piece(Color.BLUE, PieceType.WOLF): Position(2, 6),
            Piece(Color.BLUE, PieceType.CAT): Position(1, 7),
            Piece(Color.BLUE, PieceType.MOUSE): Position(6, 6),
        }

    def is_alive(self, piece: Piece) -> bool:
        return self.__piece_positions[piece] is not None

    def get_piece_position(self, piece: Piece) -> Optional[Position]:
        return self.__piece_positions[piece]

    def get_piece_position_definitely(self, piece: Piece) -> Position:
        pos = self.__piece_positions[piece]
        if pos is None:
            raise RuntimeError("Invariant not upheld: The piece is already dead")
        return pos

    def get_adjacent_cells(self, position) -> List[Cell]:
        return self.__map.get_adjacent_cells(position.x, position.y)

    def get_location(self, position: Position) -> Optional[Location]:
        return self.__map[position.x, position.y]

    def get_location_definitely(self, position: Position) -> Location:
        loc = self.__map[position.x, position.y]
        if loc is None:
            raise RuntimeError("Invariant not upheld: Invalid position")
        return loc

    def set_piece_position(self, piece: Piece, position: Position):
        self.__piece_positions[piece] = position

    def kill_piece(self, piece: Piece):
        self.__piece_positions[piece] = None
