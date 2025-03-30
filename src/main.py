from constants import SCREEN_SIZE
import pygame
import random
import datetime

pygame.init()
random.seed(datetime.datetime.now().ctime())

pygame.display.set_caption("Zombie smash")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCREEN_SIZE)

hits = 0
misses = 0
clock = pygame.time.Clock()
last_mouse_state = pygame.mouse.get_pressed()
while True:
    current_ms = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
