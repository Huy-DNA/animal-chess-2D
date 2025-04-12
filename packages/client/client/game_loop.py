import pygame
from pygame.time import Clock
from ui.offline_pvp_match_scene import OfflinePvPMatchScene
from ui.menu_scene import MenuScene
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
        self.__switch_scene(GameSceneType.MENU)

    def __switch_scene(self, scene_type: GameSceneType):
        if scene_type == GameSceneType.OFFLINE_PVP_MATCH:
            self.__current_scene = OfflinePvPMatchScene(self.__screen)
        elif scene_type == GameSceneType.MENU:
            self.__current_scene = MenuScene(self.__screen)

    def run(self):
        self.__running = True

        while self.__running:
            scene_events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                    break

                scene_events.append(event)

            next_scene_type = self.__current_scene.step(scene_events)
            if self.__current_scene.get_type() != next_scene_type:
                self.__switch_scene(next_scene_type)
            pygame.display.flip()

            self.__clock.tick(self.__fps)

        pygame.quit()
