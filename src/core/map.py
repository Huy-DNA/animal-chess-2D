from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from dataclasses import dataclass
from core.piece import Color


class Location:
    __is_river: bool
    __is_cave: Optional[Color]
    __is_trap: Optional[Color]

    def __init__(
        self, is_river: bool, is_cave: Optional[Color], is_trap: Optional[Color]
    ):
        self.__is_river = is_river
        self.__is_trap = is_trap
        self.__is_cave = is_cave

    def is_river(self) -> bool:
        return self.__is_river

    def is_cave(self) -> bool:
        return self.__is_cave is not None

    def cave_color(self) -> Color:
        if self.__is_cave is None:
            raise RuntimeError("Calling cave color on a non-cave cell")
        return self.__is_cave

    def is_trap(self) -> bool:
        return self.__is_trap is not None

    def trap_color(self) -> Color:
        if self.__is_trap is None:
            raise RuntimeError("Calling trap color on a non-trap cell")
        return self.__is_trap


@dataclass
class Cell:
    location: Location
    x: int
    y: int


class Map(ABC):
    @abstractmethod
    def width(self) -> int:
        pass

    @abstractmethod
    def height(self) -> int:
        pass

    @abstractmethod
    def __getitem__(self, indices: Tuple[int, int]) -> Optional[Location]:
        pass

    @abstractmethod
    def get_adjacent_locations(self, x: int, y: int) -> List[Cell]:
        pass


class DefaultMap(Map):
    __locations: List[List[Location]]

    def __init__(self):
        self.__locations = [
            [
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, Color.RED),
                Location(False, Color.RED, None),
                Location(False, None, Color.RED),
                Location(False, None, None),
                Location(False, None, None),
            ],
            [
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, Color.RED, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
            ],
            [
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
            ],
            [
                Location(False, None, None),
                Location(True, None, None),
                Location(True, None, None),
                Location(False, None, None),
                Location(True, None, None),
                Location(True, None, None),
                Location(False, None, None),
            ],
            [
                Location(False, None, None),
                Location(True, None, None),
                Location(True, None, None),
                Location(False, None, None),
                Location(True, None, None),
                Location(True, None, None),
                Location(False, None, None),
            ],
            [
                Location(False, None, None),
                Location(True, None, None),
                Location(True, None, None),
                Location(False, None, None),
                Location(True, None, None),
                Location(True, None, None),
                Location(False, None, None),
            ],
            [
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
            ],
            [
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, Color.BLUE, None),
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, None),
            ],
            [
                Location(False, None, None),
                Location(False, None, None),
                Location(False, None, Color.BLUE),
                Location(False, Color.BLUE, None),
                Location(False, None, Color.BLUE),
                Location(False, None, None),
                Location(False, None, None),
            ],
        ]

    def width(self) -> int:
        return len(self.__locations[0])

    def height(self) -> int:
        return len(self.__locations)

    def __getitem__(self, indices: Tuple[int, int]) -> Optional[Location]:
        if indices[0] >= self.width() or indices[0] < 0:
            return None
        if indices[1] >= self.height() or indices[1] < 0:
            return None
        return self.__locations[indices[0]][indices[1]]

    def get_adjacent_locations(self, x: int, y: int) -> List[Cell]:
        res = []
        left = self[x - 1, y]
        if left:
            res.append(Cell(left, x - 1, y))
        right = self[x + 1, y]
        if right:
            res.append(Cell(right, x + 1, y))
        up = self[x, y - 1]
        if up:
            res.append(Cell(up, x, y - 1))
        down = self[x, y + 1]
        if down:
            res.append(Cell(down, x, y + 1))
        return res
