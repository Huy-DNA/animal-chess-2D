import pygame
from pygame.event import Event
from pygame.time import Clock
from ui.match_scene import MatchScene
from ui.game_scene import GameScene, GameSceneType
from ui.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class GameLoop:
    __screen: pygame.Surface
    __running: bool
    __fps: int
    __clock: Clock
    __current_scene: GameScene

    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__running = False
        self.__fps = 60
        self.__clock = pygame.time.Clock()
        self.__switch_scene(GameSceneType.MATCH)

    def __switch_scene(self, scene_type: GameSceneType):
        if scene_type == GameSceneType.MATCH:
            self.__current_scene = MatchScene(self.__screen)

    def run(self):
        self.__running = True

        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__running = False
                        break

                if event.type in (
                    pygame.MOUSEBUTTONDOWN,
                    pygame.MOUSEBUTTONUP,
                    pygame.MOUSEMOTION,
                ):
                    next_scene_type = self.__current_scene.step(event)
                    if self.__current_scene.get_type() != next_scene_type:
                        self.__switch_scene(next_scene_type)

            if not pygame.event.get():
                self.__current_scene.step(Event(0))

            pygame.display.flip()

            self.__clock.tick(self.__fps)

        pygame.quit()
