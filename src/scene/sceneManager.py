import pygame

from src.scene.GameOverScene import GameOverScene
from src.scene.GameScene import GameScene
from src.scene.MenuScene import MenuScene
from src.utils.eventHelper import EVENT_SCENEGAME, EVENT_SCENEGAMEOVER, EVENT_SCENESTART

class SceneManager:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.currentScene = MenuScene(screen)
        
    def onEvent(self, event):
        self.currentScene.onEvent(event)
        if event.type == EVENT_SCENESTART:
            self.currentScene = MenuScene(self.screen)
        if event.type == EVENT_SCENEGAME:
            self.currentScene = GameScene(self.screen)
        if event.type == EVENT_SCENEGAMEOVER:
            self.currentScene = GameOverScene(self.screen)
        
    def onKeyDown(self, keys):
        self.currentScene.onKeyDown(keys)
        
    def onTick(self):
        if self.currentScene.nextScene != None:
            self.currentScene = self.currentScene.nextScene
        self.currentScene.update()
        self.currentScene.display()
        
    def onClick(self, position: tuple[int, int]):
        self.currentScene.onClick(position)