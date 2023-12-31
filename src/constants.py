import pygame

from .exe import pathof

VEC = pygame.math.Vector2
WIDTH, HEIGHT = 1200, 675
SCR_DIM = VEC(WIDTH, HEIGHT)
FPS = 144

GRAVITY = 1200
PIXEL_SIZE = 3
REAL_TILE_SIZE = 16
TILE_SIZE = REAL_TILE_SIZE * PIXEL_SIZE

pygame.font.init()
FONT = [pygame.font.Font(pathof("assets/fonts/PixelTandysoft-0rJG.ttf"), i) for i in range(1, 129)]
STOPPING_CHARS = {" ", "!", "$", "%", "(", "-", "+", "{", "}", "[", "|", "\\", "?"}
TEXT_COLOR = (0, 100, 220)