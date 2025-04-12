from typing import List
from pygame import Surface
import pygame
from pygame.event import Event
from client.ui.button import Button
from ui.game_scene import GameScene, GameSceneType
from ui.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)


class MenuScene(GameScene):
    def __init__(self, screen: Surface):
        self.screen = screen

        self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill((50, 100, 50))

        self.title_font = pygame.font.SysFont("Arial", 64, bold=True)
        self.button_font = pygame.font.SysFont("Arial", 36)

        button_width = 400
        button_height = 60
        button_spacing = 20
        start_y = SCREEN_HEIGHT // 2 - 100

        buttons_info = [
            "Computer vs Player",
            "Player vs Player",
            "Online",
            "Instructions",
            "Quit",
        ]

        self.buttons = []
        for i, text in enumerate(buttons_info):
            x = SCREEN_WIDTH // 2 - button_width // 2
            y = start_y + i * (button_height + button_spacing)
            self.buttons.append(
                Button(x, y, button_width, button_height, text, self.button_font)
            )

    def get_type(self) -> GameSceneType:
        return GameSceneType.MENU

    def step(self, events: List[Event]) -> GameSceneType:
        mouse_pos = pygame.mouse.get_pos()

        for button in self.buttons:
            button.update(mouse_pos)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, button in enumerate(self.buttons):
                    if button.is_clicked(mouse_pos):
                        if i == 0:
                            return GameSceneType.MATCH
                        elif i == 1:
                            return GameSceneType.MATCH
                        elif i == 2:
                            pass
                        elif i == 3:
                            pass
                        elif i == 4:
                            pygame.quit()
                            exit()

        self.draw()

        return GameSceneType.MENU

    def draw(self) -> None:
        self.screen.blit(self.background, (0, 0))

        title_text = self.title_font.render("Animal Chess", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(title_text, title_rect)

        for button in self.buttons:
            button.draw(self.screen)
