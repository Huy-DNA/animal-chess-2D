from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from pygame.event import Event


class GameSceneType(Enum):
    MENU = 0
    OFFLINE_PVP_MATCH = 1


class GameScene(ABC):
    @abstractmethod
    def step(self, events: List[Event]) -> GameSceneType:
        pass

    @abstractmethod
    def get_type(self) -> GameSceneType:
        pass
