from typing import Dict, List, Optional
from core.map import Position
from core.piece import Color, PieceType
import pygame
import os
import functools
from pygame.font import Font
from pygame.surface import Surface
from pygame.time import Clock
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TILE_SIZE,
    BOARD_COLS,
    BOARD_ROWS,
    BOARD_X,
    BOARD_Y,
    TURN_TIME_LIMIT,
)
from core.game import Game, Piece


class ClientGame:
    ASSETS_PATH = os.path.join(os.path.dirname(__file__), "assets")
    ANIMAL_IMAGES: Dict[PieceType, Surface] = ClientGame.load_animal_images()
    BACKGROUND_IMAGE: Surface = pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "board-image.png")).convert_alpha(),
        (SCREEN_WIDTH, SCREEN_HEIGHT),
    )
    INNER_BACKGROUND_IMAGE: Surface = pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "forest-bg.png")).convert(),
        (SCREEN_WIDTH, SCREEN_HEIGHT),
    )
    TRAP_IMAGE: Surface = pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "trap-image.png")),
        (TILE_SIZE, TILE_SIZE),
    )
    CAVE_IMAGE: Surface = pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "cave-image.png")),
        (TILE_SIZE, TILE_SIZE),
    )
    FONT: Font = pygame.font.SysFont(None, 36)
    CLOCK: Clock = pygame.time.Clock()

    game: Game
    screen: Surface
    turn_start_time: int
    selected_piece: Optional[Piece]
    offset_x: int
    offset_y: int

    def __init__(self):
        pygame.display.set_caption("Animal chess")
        self.game = Game()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.turn_start_time = pygame.time.get_ticks()
        self.selected_piece = None
        self.offset_x = 0
        self.offset_y = 0

    @staticmethod
    def load_animal_images():
        images = {}
        name_to_type = {
            "elephant": PieceType.ELEPHANT,
            "lion": PieceType.LION,
            "tiger": PieceType.TIGER,
            "leopard": PieceType.LEOPARD,
            "dog": PieceType.DOG,
            "wolf": PieceType.WOLF,
            "cat": PieceType.CAT,
            "mouse": PieceType.MOUSE,
        }
        for name in os.listdir(ClientGame.ASSETS_PATH):
            if name.endswith(".png") and name not in [
                "trap-image.png",
                "board-image.png",
                "forest-bg.png",
            ]:
                img = pygame.image.load(
                    os.path.join(ClientGame.ASSETS_PATH, name)
                ).convert_alpha()
                img = pygame.transform.smoothscale(img, (TILE_SIZE, TILE_SIZE))
                key = name_to_type[name.replace("-image.png", "")]
                images[key] = img
        return images

    def get_board_mouse_pos(self, mouse_x: float, mouse_y: float) -> Optional[Position]:
        col = (mouse_x - BOARD_X) // TILE_SIZE
        row = (mouse_y - BOARD_Y) // TILE_SIZE
        if 0 <= col < BOARD_COLS and 0 <= row < BOARD_ROWS:
            return Position(row, col)
        return None

    @functools.cache
    def rivers(self) -> List[Position]:
        state = self.game.get_state()
        map = state.get_map()

        river_positions = []
        for y in range(map.height()):
            for x in range(map.width()):
                location = map[y, x]
                if location and location.is_river:
                    river_positions.append(Position(x, y))

        return river_positions

    @functools.cache
    def caves(self) -> List[Position]:
        state = self.game.get_state()
        map = state.get_map()

        cave_positions = []
        for y in range(map.height()):
            for x in range(map.width()):
                location = map[y, x]
                if location and location.cave_color is not None:
                    cave_positions.append(Position(x, y))

        return cave_positions

    @functools.cache
    def traps(self) -> List[Position]:
        state = self.game.get_state()
        map = state.get_map()

        trap_positions = []
        for y in range(map.height()):
            for x in range(map.width()):
                location = map[y, x]
                if location and location.trap_color is not None:
                    trap_positions.append(Position(x, y))

        return trap_positions

    def draw_board(self):
        self.screen.blit(ClientGame.INNER_BACKGROUND_IMAGE, (0, 0))
        self.screen.blit(ClientGame.BACKGROUND_IMAGE, (0, 0))

        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                rect = pygame.Rect(
                    BOARD_X + col * TILE_SIZE,
                    BOARD_Y + row * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE,
                )
                tile_pos = Position(row, col)

                if tile_pos in self.rivers():
                    pygame.draw.rect(self.screen, (0, 150, 255), rect)
                elif tile_pos in self.traps():
                    pygame.draw.rect(self.screen, (255, 230, 200), rect)
                else:
                    pygame.draw.rect(self.screen, (245, 222, 179), rect)

                if tile_pos not in self.rivers():
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

                if tile_pos in self.caves():
                    self.screen.blit(ClientGame.CAVE_IMAGE, rect.topleft)

                if tile_pos in self.traps():
                    self.screen.blit(ClientGame.TRAP_IMAGE, rect.topleft)

                piece = self.game.get_state().get_piece_at_position(tile_pos)
                if piece and piece != self.selected_piece:
                    img = ClientGame.ANIMAL_IMAGES[piece.type]
                    center = (rect.centerx, rect.centery)
                    pygame.draw.circle(
                        self.screen, (255, 255, 255), center, TILE_SIZE // 2 - 4
                    )

                    img_rect = img.get_rect(center=center)
                    self.screen.blit(img, img_rect.topleft)

                    team_color = (
                        (255, 0, 0) if piece.color == Color.RED else (0, 0, 255)
                    )
                    pygame.draw.circle(
                        self.screen, team_color, center, TILE_SIZE // 2 - 4, 4
                    )

        turn_text = ClientGame.FONT.render(
            f"{self.game.get_turn().to_string().upper()}'s TURN",
            True,
            (255, 0, 0) if self.game.get_turn() == Color.RED else (0, 0, 255),
        )
        self.screen.blit(turn_text, (20, 20))
        elapsed = pygame.time.get_ticks() - self.turn_start_time
        remaining = max(0, TURN_TIME_LIMIT - elapsed)
        seconds_left = remaining // 1000

        timer_text = ClientGame.FONT.render(f"{seconds_left}s", True, (0, 0, 0))
        self.screen.blit(timer_text, (20, 60))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = self.get_board_mouse_pos(*pygame.mouse.get_pos())
                    if pos is not None:
                        piece = self.game.get_state().get_piece_at_position(pos)
                        if piece and piece.color == self.game.get_turn():
                            self.selected_piece = piece
                            self.offset_x = pos.y - (BOARD_X + pos.x * TILE_SIZE)
                            self.offset_y = pos.x - (BOARD_Y + pos.y * TILE_SIZE)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.selected_piece:
                        mx, my = event.pos
                        pos = self.get_board_mouse_pos(mx, my)
                        if pos is not None:
                            moved = self.game.move(self.selected_piece, pos)
                            if moved:
                                self.turn_start_time = pygame.time.get_ticks()
                        self.selected_piece = None

            self.draw_board()

            if self.selected_piece:
                mx, my = pygame.mouse.get_pos()
                img = ClientGame.ANIMAL_IMAGES[self.selected_piece.type]
                pygame.draw.circle(
                    self.screen, (255, 255, 255), (mx, my), TILE_SIZE // 2 - 4
                )
                img_rect = img.get_rect(center=(mx, my))
                self.screen.blit(img, img_rect.topleft)

                team_color = (
                    (255, 0, 0)
                    if self.selected_piece.color == Color.RED
                    else (0, 0, 255)
                )
                pygame.draw.circle(
                    self.screen, team_color, (mx, my), TILE_SIZE // 2 - 4, 4
                )

            pygame.display.flip()
            ClientGame.CLOCK.tick(60)

        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    game = ClientGame()
    game.run()
