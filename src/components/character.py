import pygame

from src.components.gameEntity import GameEntity
from src.player import Player
from src.components.movable import Movable

class Character(GameEntity, Movable):
    def __init__(self):
        GameEntity.__init__(self, 'assets/player.png', 0, 0, 60, 50)
        self.player = Player.getPlayer()
        self.speed = 14
        Movable.__init__(self, self.speed, self.rect)
        
    def update(self):
        self.player.distance = self.player.distance + 1