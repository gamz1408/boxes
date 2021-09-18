import os
from random import randint
import sys

import pygame

from cell import *
from constants import *
from game_registry import *


pygame.display.set_caption('Cells')

game_registry = GameRegistry()

'''
box_group = pygame.sprite.Group()
for i in range(10):
    box_group.add(Box(randint(1, 10), randint(1, 10)))
'''

def spawn_cell():
    pass
    
def draw_window():
    WIN.fill(SKYBLUE)
    WIN.fill(WHITE, (SIMULATION_WIDTH, 0, WIDTH, HEIGHT))
    #box_group.draw(WIN)
    #box_group.update()
    #pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    run = True 
    
    #game_registry.add_cell(100, 100, 30, 30, 1, BLACK)
    #game_registry.add_cell(300, 100, 30, 30, 1, BLACK)

    game_registry.populate(10, 30, 30, 1, BLACK, awareness_radius=40)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print(game_registry.claimed_positions_registry)
                print('Goodbye!')
                
        # keysPressed = pygame.key.get_pressed()
        
        draw_window()
        game_registry.update_cells()
        pygame.display.update()

        
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
