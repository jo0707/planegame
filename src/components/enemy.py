import pygame
import random
import config
from src.components.movable import Movable
from src.utils.screenHelper import ScreenHelper

class Enemy(pygame.sprite.Sprite, Movable):
    def __init__(self):
        pygame.sprite.Sprite().__init__()
        self.surf = pygame.image.load('assets/enemy.png')
        self.surf = pygame.transform.scale(self.surf, (60,50))
        self.rect = self.surf.get_rect(
            center=(
                pygame.display.get_window_size()[0] + 20,
                random.randint(0, pygame.display.get_window_size()[1]),
            )
        )
        self.speed = 5
        Movable.__init__(self, ScreenHelper.getWindowX(), random.randint(0, ScreenHelper.getWindowY()), 5, pygame.Rect(0, 0, 60, 50))
        
    def update(self) -> None:
        self.moveLeft()