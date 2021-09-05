import pygame, os, sys
from classA import *
from constants import *
from random import randint
# any questions maybe
# i wonder how can you launch it, if it was all in one file maybe would be better 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Xazar Warrior')

box = pygame.sprite.Group()
for i in range(10):
    box.add(Box(randint(1, 10), randint(1, 10)))
    
    
def draw_window():
    WIN.fill(SKYBLUE)
    box.draw(WIN)
    box.update()
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True 
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        # keysPressed = pygame.key.get_pressed()
        
        draw_window()
        
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
