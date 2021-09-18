import pygame, os

COS45 = 0.7

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKYBLUE = (146, 244, 255)

FPS = 60

WIDTH = 1200
HEIGHT = 600
SIMULATION_WIDTH = 600

BOX = pygame.image.load(os.path.join('assets', 'box.png'))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

CELL_TARGET_ACCURACY = 3