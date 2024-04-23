import pygame

from src.scene.GameOverScene import GameOverScene
from src.components.character import Character
from src.components.coin import Coin
from src.components.enemy import Enemy
from src.components.button import Button
from src.components.clickable import Clickable
from src.scene.scene import Scene
from src.utils.screenHelper import ScreenHelper
from src.utils.fontHelper import fonts
from src.utils.eventHelper import EVENT_NEWCOIN, EVENT_NEWENEMY

class GameScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        pygame.time.set_timer(EVENT_NEWENEMY, 1000)
        pygame.time.set_timer(EVENT_NEWCOIN, 7000)
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        self.enemySprites = pygame.sprite.Group()
        self.coinSprites = pygame.sprite.Group()
        self.character = Character()
        self.sprites.add(self.character)
        self.sprites.add(self.enemySprites)
        self.sprites.add(self.coinSprites)
    
    def onKeyDown(self, keys):
        if keys[pygame.K_UP]:
            self.character.moveUp()
        if keys[pygame.K_DOWN]:
            self.character.moveDown()
        if keys[pygame.K_LEFT]:
            self.character.moveLeft()
        if keys[pygame.K_RIGHT]:
            self.character.moveRight()
    
    def onEvent(self, event):
        if event == EVENT_NEWENEMY:
            newEnemy = Enemy()
            self.enemySprites.add(newEnemy)
            self.sprites.add(newEnemy)
            
        if event == EVENT_NEWCOIN:
            newCoin = Coin()
            self.coinSprites.add(newCoin)
            self.sprites.add(newCoin)
    
    def onClick(self, position: tuple[int, int]):
        for sprite in self.sprites:
            if sprite.rect.collidepoint(position) and isinstance(sprite, Clickable):
                sprite.onClick()
    
    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)
    
    def update(self):
        for sprite in self.sprites:
            sprite.update()
        
        for coinSprite in self.coinSprites:
            if pygame.sprite.collide_rect(coinSprite, self.character):
                self.coinSprites.remove(coinSprite)
                self.sprites.remove(coinSprite)
                self.character.coins = self.character.coins + 1
            
        if pygame.sprite.spritecollideany(self.character, self.enemySprites):
            self.switchToScene(GameOverScene(self.screen))    
            
        