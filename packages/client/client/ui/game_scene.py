from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional
from pygame.event import Event


class GameSceneType(Enum):
    MENU = 0
    OFFLINE_PVP_MATCH = 1
    OFFLINE_CVP_MATCH = 2
    DIFFICULTY_MENU = 3


class GameScene(ABC):
    @abstractmethod
    def step(self, events: List[Event]) -> Optional["GameScene"]:
        pass

    @abstractmethod
    def get_type(self) -> GameSceneType:
        pass
