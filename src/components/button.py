import pygame
import random

from src.components.clickable import Clickable

class Button(pygame.sprite.Sprite, Clickable):
    def __init__(self, x: int, y: int, width: int, height: int, text: str, font: pygame.font.Font, textColor: tuple[int, int, int] = pygame.colordict.THECOLORS["white"], action=lambda: None) -> None:
        pygame.sprite.Sprite.__init__(self)
        
        # import from assets
        self.image = pygame.image.load("assets/button.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.text = font.render(text, True, textColor)
        # self.hoverText = font.render(text, True, hoverColor)
        self.action = action
        # self.hoverColor = hoverColor
        self.hover = False
        #put text in the middle of the button
        self.textRect = self.text.get_rect(center=(width // 2, height // 2))
        self.image.blit(self.text, self.textRect)
        

    def update(self):
        # if self.hover:
        #     self.image.fill(self.hoverColor)
        #     self.image.blit(self.hoverText, (0, 0))
        # else:
        #     self.image.fill(self.color)
        #     self.image.blit(self.text, (0, 0))
        pass

    def onClick(self):
        self.action()

    def onHover(self):
        self.hover = True

    def onUnhover(self):
        self.hover = False