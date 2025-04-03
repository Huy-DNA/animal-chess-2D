from abc import ABC, abstractmethod
from enum import Enum


class Color(Enum):
    RED = 0
    BLUE = 1


class Piece(ABC):
    __color: Color
    __current_level: int

    def __init__(self, color: Color):
        self.__color = color
        self.__current_level = self.get_default_level()

    @abstractmethod
    def can_cross_river(self) -> bool:
        pass

    @abstractmethod
    def can_jump_river(self) -> bool:
        pass

    @abstractmethod
    def get_default_level(self) -> int:
        pass

    @abstractmethod
    def can_eat(self, other: "Piece") -> bool:
        pass

    @abstractmethod
    def can_be_eaten(self, other: "Piece") -> bool:
        pass

    def get_color(self) -> Color:
        return self.__color

    def get_current_level(self) -> int:
        return self.__current_level

    def set_current_level(self, level: int):
        self.__current_level = level


class ElephantPiece(Piece):
    LEVEL: int = 8

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def can_eat(self, other: "Piece") -> bool:
        return other.get_current_level() <= self.get_current_level()

    def can_be_eaten(self, other: "Piece") -> bool:
        return (
            other.get_current_level() >= self.get_current_level()
            or type(other) is MousePiece
        )


class LionPiece(Piece):
    LEVEL: int = 7

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return True

    def get_default_level(self) -> int:
        return self.LEVEL

    def can_eat(self, other: "Piece") -> bool:
        return other.get_current_level() <= self.get_current_level()

    def can_be_eaten(self, other: "Piece") -> bool:
        return other.get_current_level() >= self.get_current_level()


class TigerPiece(Piece):
    LEVEL: int = 6

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return True

    def get_default_level(self) -> int:
        return self.LEVEL

    def can_eat(self, other: "Piece") -> bool:
        return other.get_current_level() <= self.get_current_level()

    def can_be_eaten(self, other: "Piece") -> bool:
        return other.get_current_level() >= self.get_current_level()


class LeopardPiece(Piece):
    LEVEL: int = 5

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def can_eat(self, other: "Piece") -> bool:
        return other.get_current_level() <= self.get_current_level()

    def can_be_eaten(self, other: "Piece") -> bool:
        return other.get_current_level() >= self.get_current_level()


class DogPiece(Piece):
    LEVEL: int = 4

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def can_eat(self, other: "Piece") -> bool:
        return other.get_current_level() <= self.get_current_level()

    def can_be_eaten(self, other: "Piece") -> bool:
        return other.get_current_level() >= self.get_current_level()


class WolfPiece(Piece):
    LEVEL: int = 3

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def can_eat(self, other: "Piece") -> bool:
        return other.get_current_level() <= self.get_current_level()

    def can_be_eaten(self, other: "Piece") -> bool:
        return other.get_current_level() >= self.get_current_level()


class CatPiece(Piece):
    LEVEL: int = 2

    def can_cross_river(self) -> bool:
        return False

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def can_eat(self, other: "Piece") -> bool:
        return other.get_current_level() <= self.get_current_level()

    def can_be_eaten(self, other: "Piece") -> bool:
        return other.get_current_level() >= self.get_current_level()


class MousePiece(Piece):
    LEVEL: int = 1

    def can_cross_river(self) -> bool:
        return True

    def can_jump_river(self) -> bool:
        return False

    def get_default_level(self) -> int:
        return self.LEVEL

    def can_eat(self, other: "Piece") -> bool:
        return (
            other.get_current_level() <= self.get_current_level()
            or type(other) is ElephantPiece
        )

    def can_be_eaten(self, other: "Piece") -> bool:
        return other.get_current_level() >= self.get_current_level()
