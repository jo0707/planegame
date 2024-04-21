import pygame

class Movable:
    def __init__(self, x: int, y: int, speed: int, rect: pygame.Rect):
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = rect
        
    def moveTo(self, x: int, y: int):
        self.x = x
        self.y = y
        self.rect.move_ip(self.x, self.y)
        
    def moveUp(self, amount: int = 0):
        self.y -= amount if amount > 0 else self.speed
        self.rect.move_ip(0, -amount)
        
    def moveDown(self, amount: int = 0):
        self.y += amount if amount > 0 else self.speed
        self.rect.move_ip(0, amount)
        
    def moveLeft(self, amount: int = 0):
        self.x -= amount if amount > 0 else self.speed
        self.rect.move_ip(-amount, 0)
        
    def moveRight(self, amount: int = 0):
        self.x += amount if amount > 0 else self.speed
        self.rect.move_ip(amount, 0)