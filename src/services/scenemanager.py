import pygame

from src.scene.MenuScene import MenuScene

class SceneManager:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.currentScene = MenuScene(screen)
    
    def GoToScene(self, scene): 
        self.currentScene = scene
        
    def onTick(self):
        self.currentScene.update()
        self.currentScene.display()
        
    def onClick(self, position: tuple[int, int]):
        self.currentScene.onClick(position)