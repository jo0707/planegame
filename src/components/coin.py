import pygame
import random

from src.components.movable import Movable
from src.utils.screenHelper import ScreenHelper

class Coin(pygame.sprite.Sprite, Movable):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('assets/coin.gif')
        self.surf = pygame.transform.scale(self.surf, (60,60))
        self.rect = self.surf.get_rect(
            center=(
                pygame.display.get_window_size()[0] + 20,
                random.randint(0, pygame.display.get_window_size()[1]),
            )
        )
        self.speed = 5
        Movable.__init__(self, ScreenHelper.getWindowX(), random.randrange(0, ScreenHelper.getWindowY()), 5, pygame.Rect(0, 0, 60, 60))
        
    def update(self) -> None:
        self.moveLeft()