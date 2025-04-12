from abc import ABC, abstractmethod
from enum import Enum
from pygame.event import Event


class GameSceneType(Enum):
    MENU = 0
    MATCH = 1


class GameScene(ABC):
    @abstractmethod
    def step(self, mouse_event: Event) -> GameSceneType:
        pass

    @abstractmethod
    def get_type(self) -> GameSceneType:
        pass
