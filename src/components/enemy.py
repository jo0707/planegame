import pygame
import random
from src.components.gameEntity import GameEntity
from src.components.movable import Movable
from src.utils.screenHelper import ScreenHelper

class Enemy(GameEntity, Movable):
    def __init__(self):
        GameEntity.__init__(self, 'assets/enemy.png', 0, 0, 60, 50)
        self.rect.center=(
            pygame.display.get_window_size()[0] + 20,
            random.randint(0, pygame.display.get_window_size()[1]),
        )        
        self.speed = 4
        Movable.__init__(self, 5, self.rect)
        
    def update(self):
        self.moveLeft()