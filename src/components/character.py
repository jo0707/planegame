import pygame

from src.components.movable import Movable

class Character(pygame.sprite.Sprite, Movable):
    def __init__(self):
        pygame.sprite.Sprite().__init__()
        self.surf = pygame.image.load('assets/player.png')
        self.surf = pygame.transform.scale(self.surf, (60,50))
        self.rect = self.surf.get_rect()
        self.speed = 8
        self.score = 0
        self.distance = 0
        Movable.__init__(self, 0, 0, 8, pygame.Rect(0, 0, 60, 50))