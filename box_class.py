import pygame, os
from constants import *
from random import randint

class Box(pygame.sprite.Sprite):
    def __init__(self, speedX, speedY):
        super().__init__()
        self.image = BOX
        self.rect = self.image.get_rect(topleft=(randint(100, 700), randint(100, 500)))
        self.speedX = speedX
        self.speedY = speedY
        
    def move(self):
        self.rect.x += self.speedX
        if self.rect.x > WIDTH - self.rect.width or self.rect.x < 0:
            self.speedX *= -1
        self.rect.y += self.speedY
        if self.rect.y > HEIGHT - self.rect.height or self.rect.y < 0:
            self.speedY *= -1        
            
    def update(self):
        self.move()