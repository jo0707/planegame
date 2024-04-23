import pygame
import random

from src.components.movable import Movable
from src.utils.screenHelper import ScreenHelper

class Coin(pygame.sprite.Sprite, Movable):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/coin.gif')
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect(
            center=(
                pygame.display.get_window_size()[0] + 20,
                random.randint(0, pygame.display.get_window_size()[1]),
            )
        )
        self.speed = 5
        Movable.__init__(self, ScreenHelper.getWindowX(), random.randrange(0, ScreenHelper.getWindowY()), 5, self.rect)
        
    def update(self):
        self.moveLeft()