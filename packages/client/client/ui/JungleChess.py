import pygame
import os
from GameState import GameState
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, BOARD_COLS, BOARD_ROWS, BOARD_HEIGHT, BOARD_WIDTH, BOARD_X, BOARD_Y, TURN_TIME_LIMIT

class JungleChessGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cờ Thú")

        # Load background
        ASSETS_PATH = os.path.join(os.path.dirname(__file__), "assets")
        self.background_image = pygame.image.load(os.path.join(ASSETS_PATH, "board-image.png")).convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.inner_background_image = pygame.image.load(os.path.join(ASSETS_PATH, "forest-bg.png")).convert()
        self.inner_background_image = pygame.transform.scale(self.inner_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Load overlays
        self.trap_image = pygame.image.load(os.path.join(ASSETS_PATH, "trap-image.png"))
        self.trap_image = pygame.transform.scale(self.trap_image, (TILE_SIZE, TILE_SIZE))

        self.den_image = pygame.image.load(os.path.join(ASSETS_PATH, "cave-image.png"))
        self.den_image = pygame.transform.scale(self.den_image, (TILE_SIZE, TILE_SIZE))

        self.font = pygame.font.SysFont(None, 36)
        self.clock = pygame.time.Clock()

        self.game_state = GameState()
        self.selected_animal = None
        self.offset_x = 0
        self.offset_y = 0

        self.animal_images = self.load_animal_images(ASSETS_PATH)

        self.turn_start_time = pygame.time.get_ticks()
        self.font = pygame.font.SysFont(None, 36)

    def load_animal_images(self, path):
        images = {}
        for name in os.listdir(path):
            if name.endswith(".png") and name not in ["trap-image.png", "board-image.png", "forest-bg.png"]:
                img = pygame.image.load(os.path.join(path, name)).convert_alpha()
                img = pygame.transform.smoothscale(img, (TILE_SIZE, TILE_SIZE))
                key = name.replace("-image.png", "")
                images[key] = img
        return images

    def get_board_pos(self, x, y):
        col = (x - BOARD_X) // TILE_SIZE
        row = (y - BOARD_Y) // TILE_SIZE
        if 0 <= col < BOARD_COLS and 0 <= row < BOARD_ROWS:
            return row, col
        return None, None

    def draw_board(self):
        self.screen.blit(self.inner_background_image, (0, 0))
        self.screen.blit(self.background_image, (0, 0))

        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                rect = pygame.Rect(BOARD_X + col * TILE_SIZE, BOARD_Y + row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                tile_pos = (row, col)

                if tile_pos in self.game_state.rivers:
                    pygame.draw.rect(self.screen, (0, 150, 255), rect)
                elif tile_pos in self.game_state.traps:
                    pygame.draw.rect(self.screen, (255, 230, 200), rect)
                else:
                    pygame.draw.rect(self.screen, (245, 222, 179), rect)

                if tile_pos not in self.game_state.rivers:
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

                if tile_pos in self.game_state.dens.values():
                    self.screen.blit(self.den_image, rect.topleft)

                if tile_pos in self.game_state.traps:
                    self.screen.blit(self.trap_image, rect.topleft)

                animal = self.game_state.animals.get(tile_pos)
                if animal and animal != self.selected_animal:
                    img = self.animal_images[animal.name]
                    center = (rect.centerx, rect.centery)
                    pygame.draw.circle(self.screen, (255, 255, 255), center, TILE_SIZE // 2 - 4)

                    img_to_draw = img
                    if animal.frozen:
                        frozen_img = img.copy()
                        frozen_img.fill((100, 100, 100, 180), special_flags=pygame.BLEND_RGBA_MULT)
                        img_to_draw = frozen_img

                    img_rect = img_to_draw.get_rect(center=center)
                    self.screen.blit(img_to_draw, img_rect.topleft)

                    team_color = (255, 0, 0) if animal.team == 'red' else (0, 0, 255)
                    pygame.draw.circle(self.screen, team_color, center, TILE_SIZE // 2 - 4, 4)

        turn_text = self.font.render(f"{self.game_state.turn.upper()}'s TURN", True, (255, 0, 0) if self.game_state.turn == 'red' else (0, 0, 255))
        self.screen.blit(turn_text, (20, 20))
        # Hiển thị thời gian còn lại
        elapsed = pygame.time.get_ticks() - self.turn_start_time
        remaining = max(0, TURN_TIME_LIMIT - elapsed)
        seconds_left = remaining // 1000

        timer_text = self.font.render(f"{seconds_left}s", True, (0, 0, 0))
        self.screen.blit(timer_text, (20, 60))


    def run(self):
        running = True                
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_board_pos(*pos)
                    if row is not None and col is not None:
                        animal = self.game_state.animals.get((row, col))
                        if animal and animal.team == self.game_state.turn and not animal.frozen:
                            self.selected_animal = animal
                            self.offset_x = pos[0] - (BOARD_X + col * TILE_SIZE)
                            self.offset_y = pos[1] - (BOARD_Y + row * TILE_SIZE)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.selected_animal:
                        mx, my = event.pos
                        row, col = self.get_board_pos(mx, my)
                        if row is not None and col is not None:
                            moved = self.game_state.move_animal(self.selected_animal, row, col)                            
                            if moved:
                                self.turn_start_time = pygame.time.get_ticks()
                        self.selected_animal = None

            self.draw_board()

            if self.selected_animal:
                mx, my = pygame.mouse.get_pos()
                img = self.animal_images[self.selected_animal.name]
                pygame.draw.circle(self.screen, (255, 255, 255), (mx, my), TILE_SIZE // 2 - 4)
                img_rect = img.get_rect(center=(mx, my))
                self.screen.blit(img, img_rect.topleft)

                team_color = (255, 0, 0) if self.selected_animal.team == 'red' else (0, 0, 255)
                pygame.draw.circle(self.screen, team_color, (mx, my), TILE_SIZE // 2 - 4, 4)

            # Kiểm tra hết giờ
            elapsed = pygame.time.get_ticks() - self.turn_start_time
            if elapsed > TURN_TIME_LIMIT:
                self.game_state.turn = 'blue' if self.game_state.turn == 'red' else 'red'
                self.turn_start_time = pygame.time.get_ticks()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

# if __name__ == '__main__':
#     jungleGame = JungleChessGame()
#     jungleGame.run()