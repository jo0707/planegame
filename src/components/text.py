import pygame

class Text():
    def __init__(self, font, text, x, y, size, color, bgColor = None):
        self.font = pygame.font.SysFont(font, size)
        self.text = text
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        
        self.surf = self.font.render(text, True, color, bgColor)
        self.rect = self.surf.get_rect()
        self.rect.topleft = (x, y)
        