import pygame

from src.scene.MenuScene import MenuScene

class SceneManager:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.currentScene = MenuScene(screen)
        
    def onEvent(self, event):
        self.currentScene.onEvent(event)
        
    def onKeyDown(self, keys):
        self.currentScene.onKeyDown(keys)
        
    def onTick(self):
        if self.currentScene.nextScene != None:
            self.currentScene = self.currentScene.nextScene
        self.currentScene.update()
        self.currentScene.display()
        
    def onClick(self, position: tuple[int, int]):
        self.currentScene.onClick(position)