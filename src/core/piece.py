from abc import ABC, abstractmethod
from enum import Enum


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


class ElephantPiece(Piece):
    LEVEL: int = 8

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL


class LionPiece(Piece):
    LEVEL: int = 7

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return True

    def get_default_level(self) -> int:
        return self.LEVEL


class TigerPiece(Piece):
    LEVEL: int = 6

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return True

    def get_default_level(self) -> int:
        return self.LEVEL


class LeopardPiece(Piece):
    LEVEL: int = 5

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL


class DogPiece(Piece):
    LEVEL: int = 4

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL


class WolfPiece(Piece):
    LEVEL: int = 3

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL


class CatPiece(Piece):
    LEVEL: int = 2

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL


class MousePiece(Piece):
    LEVEL: int = 1

    def can_cross_river(self) -> bool:
        return True

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL
