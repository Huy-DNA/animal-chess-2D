import os

from sprites.SpriteMap import loadSpriteMap

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

ASSETS_DIR = f"{os.getcwd()}/assets"

SPRITE_PATHS = []

SPRITE_MAP = loadSpriteMap(SPRITE_PATHS)
