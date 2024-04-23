import pygame
import random

from src.components.gameEntity import GameEntity
from src.components.movable import Movable

class Coin(GameEntity, Movable):
    def __init__(self):
        GameEntity.__init__(self, 'assets/coin.gif', 0, 0, 60, 60)
        self.rect.center = (            
            pygame.display.get_window_size()[0] + 20,
            random.randint(0, pygame.display.get_window_size()[1]),
        )
        self.speed = 5
        Movable.__init__(self, 5, self.rect)
        
    def update(self):
        self.moveLeft()