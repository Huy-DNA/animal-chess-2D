from typing import List, Optional
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


class Map:
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

    def __getitem__(self, x: int, y: int) -> Location:
        if x >= self.width() or x < 0:
            raise RuntimeError("Invalid index x")
        if y >= self.height() or y < 0:
            raise RuntimeError("Invalid index y")
        return self.__locations[x][y]

    def at(self, x: int, y: int) -> Optional[Location]:
        if x >= self.width() or x < 0:
            return None
        if y >= self.height() or y < 0:
            return None
        return self.__locations[x][y]

    def get_adjacent_locations(self, x: int, y: int) -> List[Cell]:
        res = []
        left = self.at(x - 1, y)
        if left:
            res.append(Cell(left, x - 1, y))
        right = self.at(x + 1, y)
        if right:
            res.append(Cell(right, x + 1, y))
        up = self.at(x, y - 1)
        if up:
            res.append(Cell(up, x, y - 1))
        down = self.at(x, y + 1)
        if down:
            res.append(Cell(down, x, y + 1))
        return res
