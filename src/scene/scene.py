from abc import ABC, abstractmethod
import pygame

class Scene(ABC):
    def __init__(self, screen: pygame.Surface):
        self.nextScene = None
        self.sprites = pygame.sprite.Group()
        self.screen = screen
    
    @abstractmethod
    def onKeyDown(self, key):
        pass

    @abstractmethod
    def onClick(self, position: tuple[int, int]):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def SwitchToScene(self, nextScene):
        self.nextScene = nextScene
