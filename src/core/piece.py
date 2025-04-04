from abc import ABC, abstractmethod
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


class Piece(ABC):
    __color: Color

    def __init__(self, color: Color):
        self.__color = color

    @abstractmethod
    def can_cross_river(self) -> bool:
        pass

    @abstractmethod
    def can_jump_river(self) -> bool:
        pass

    @abstractmethod
    def get_default_level(self) -> int:
        pass

    def get_color(self) -> Color:
        return self.__color

    @abstractmethod
    def get_type(self) -> PieceType:
        pass


class ElephantPiece(Piece):
    LEVEL: int = 8
    TYPE: PieceType = PieceType.ELEPHANT

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def get_type(self) -> PieceType:
        return self.TYPE


class LionPiece(Piece):
    LEVEL: int = 7
    TYPE: PieceType = PieceType.LION

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return True

    def get_default_level(self) -> int:
        return self.LEVEL

    def get_type(self) -> PieceType:
        return self.TYPE


class TigerPiece(Piece):
    LEVEL: int = 6
    TYPE: PieceType = PieceType.TIGER

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return True

    def get_default_level(self) -> int:
        return self.LEVEL

    def get_type(self) -> PieceType:
        return self.TYPE


class LeopardPiece(Piece):
    LEVEL: int = 5
    TYPE: PieceType = PieceType.LEOPARD

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def get_type(self) -> PieceType:
        return self.TYPE


class DogPiece(Piece):
    LEVEL: int = 4
    TYPE: PieceType = PieceType.DOG

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def get_type(self) -> PieceType:
        return self.TYPE


class WolfPiece(Piece):
    LEVEL: int = 3
    TYPE: PieceType = PieceType.WOLF

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def get_type(self) -> PieceType:
        return self.TYPE


class CatPiece(Piece):
    LEVEL: int = 2
    TYPE: PieceType = PieceType.CAT

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def get_type(self) -> PieceType:
        return self.TYPE


class MousePiece(Piece):
    LEVEL: int = 1
    TYPE: PieceType = PieceType.MOUSE

    def can_cross_river(self) -> bool:
        return True

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def get_type(self) -> PieceType:
        return self.TYPE
