import pygame

from src.scene.GameScene import GameScene
from src.components.button import Button
from src.components.clickable import Clickable
from src.scene.scene import Scene
from src.utils.screenHelper import ScreenHelper
from src.utils.fontHelper import fonts
from src.utils.eventHelper import EVENT_SCENEGAME

class MenuScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        self.sprites.add(
            Button(
                x=ScreenHelper.getWindowX() // 2 - 100,
                y=ScreenHelper.getWindowY() // 2 - 50,
                width=200,
                height=100,
                text="Start",
                font=fonts["pixel"],
                action=lambda: self.switchSceneEvent(EVENT_SCENEGAME)
            )
        )
        self.sprites.add(
            Button(
                x=ScreenHelper.getWindowX() // 2 - 100,
                y=ScreenHelper.getWindowY() // 2 + 100,
                width=200,
                height=100,
                text="Quit",
                font=fonts["pixel"],
                action=lambda: pygame.event.post(pygame.event.Event(pygame.QUIT)),
            )
        )
    
    def onKeyDown(self, keys):
        pass
    
    def onEvent(self, event):
        pass
    
    def onClick(self, position: tuple[int, int]):
        for sprite in self.sprites:
            if sprite.rect.collidepoint(position) and isinstance(sprite, Clickable):
                sprite.onClick()
    
    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)
    
    def update(self):
        self.sprites.update()
    