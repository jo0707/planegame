import pygame

class Player():
    def __init__(self):
        self.name = "Player"
        self.coins = 0
        self.distance = 0
        
    def reset(self):
        self.coins = 0
        self.distance = 0
        self.name = "Player"