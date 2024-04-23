from abc import ABC, abstractmethod
import pygame

class Scene(ABC):
    def __init__(self, screen: pygame.Surface):
        self.nextScene = None
        self.sprites = pygame.sprite.Group()
        self.screen = screen
        
    @abstractmethod
    def onEvent(self, event):
        pass
    
    @abstractmethod
    def onKeyDown(self, keys):
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

    def switchToScene(self, nextScene):
        self.nextScene = nextScene
