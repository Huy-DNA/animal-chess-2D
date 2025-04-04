from typing import List, Optional, Tuple
from dataclasses import dataclass
from core.piece import Color


@dataclass(frozen=True)
class Location:
    is_river: bool
    cave_color: Optional[Color]
    trap_color: Optional[Color]


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass(frozen=True)
class Cell:
    location: Location
    position: Position


@dataclass(frozen=True)
class Map:
    locations: List[List[Location]]

    def width(self) -> int:
        return len(self.locations[0])

    def height(self) -> int:
        return len(self.locations)

    def __getitem__(self, indices: Tuple[int, int]) -> Optional[Location]:
        if indices[0] >= self.width() or indices[0] < 0:
            return None
        if indices[1] >= self.height() or indices[1] < 0:
            return None
        return self.locations[indices[0]][indices[1]]

    def get_adjacent_locations(self, x: int, y: int) -> List[Cell]:
        res = []
        left = self[x - 1, y]
        if left:
            res.append(Cell(left, Position(x - 1, y)))
        right = self[x + 1, y]
        if right:
            res.append(Cell(right, Position(x + 1, y)))
        up = self[x, y - 1]
        if up:
            res.append(Cell(up, Position(x, y - 1)))
        down = self[x, y + 1]
        if down:
            res.append(Cell(down, Position(x, y + 1)))
        return res


DEFAULT_MAP = Map(
    [
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
)
