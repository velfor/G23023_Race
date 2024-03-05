import pygame
from settings import *
from random import randint

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, SC_WIDTH - OBS_WIDTH)
        self.rect.bottom = 0
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top >= SC_HEIGHT:
            self.rect.x = randint(0, SC_WIDTH - OBS_WIDTH)
            self.rect.bottom = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
