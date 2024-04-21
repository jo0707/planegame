import pygame
import random

from src.components.clickable import Clickable

class Button(pygame.sprite.Sprite, Clickable):
    def __init__(self, x: int, y: int, width: int, height: int, text: str, font: pygame.font.Font, color: tuple[int, int, int], action) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.text = font.render(text, True, color)
        # self.hoverText = font.render(text, True, hoverColor)
        self.action = action
        self.color = color
        # self.hoverColor = hoverColor
        self.hover = False

    def update(self) -> None:
        if self.hover:
            self.surf.fill(self.hoverColor)
            self.surf.blit(self.hoverText, (0, 0))
        else:
            self.surf.fill(self.color)
            self.surf.blit(self.text, (0, 0))

    def onClick(self) -> None:
        self.action()

    def onHover(self) -> None:
        self.hover = True

    def onUnhover(self) -> None:
        self.hover = False