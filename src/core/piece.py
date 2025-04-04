from dataclasses import dataclass
from enum import Enum


class PieceType(Enum):
    MOUSE = 0
    CAT = 1
    WOLF = 2
    DOG = 3
    LEOPARD = 4
    TIGER = 5
    LION = 6
    ELEPHANT = 7


class Color(Enum):
    RED = 0
    BLUE = 1


@dataclass(frozen=True)
class Piece:
    color: Color
    type: PieceType

    def can_cross_river(self) -> bool:
        return self.type == PieceType.MOUSE

    def can_jump_river(self) -> bool:
        return self.type == PieceType.LION or self.type == PieceType.TIGER

    def get_default_level(self) -> int:
        return self.type
