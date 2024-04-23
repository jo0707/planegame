import pygame

from src.components.textbox import Textbox
from src.components.character import Character
from src.components.coin import Coin
from src.components.enemy import Enemy
from src.components.clickable import Clickable
from src.scene.scene import Scene
from src.utils.eventHelper import EVENT_NEWCOIN, EVENT_NEWENEMY, EVENT_SCENEGAMEOVER

class GameScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        pygame.time.set_timer(EVENT_NEWENEMY, 200)
        pygame.time.set_timer(EVENT_NEWCOIN, 5000)
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        self.enemySprites = pygame.sprite.Group()
        self.coinSprites = pygame.sprite.Group()
        self.character = Character()
        self.distanceText = Textbox("Distance: 0", x=10, y=10)
        self.coinsText = Textbox("Coins: 0", x=10, y=40)
        self.textboxes += [self.distanceText, self.coinsText]
        self.sprites.add(self.character)
        self.sprites.add(self.enemySprites)
        self.sprites.add(self.coinSprites)
    
    def onKeyDown(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.character.moveUp()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.character.moveDown()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.character.moveLeft()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.character.moveRight()
    
    def onEvent(self, event):
        if event.type == EVENT_NEWENEMY:
            newEnemy = Enemy()
            self.enemySprites.add(newEnemy)
            self.sprites.add(newEnemy)
        if event.type == EVENT_NEWCOIN:
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
        for textbox in self.textboxes:
            textbox.display(self.screen)
    
    def update(self):
        for sprite in self.sprites:
            sprite.update()
        
        self.distanceText.setText(f"Distance: {self.character.player.distance}")
        self.coinsText.setText(f"Coins: {self.character.player.coins}")
        
        for coinSprite in self.coinSprites:
            if pygame.sprite.collide_rect(coinSprite, self.character):
                pygame.mixer.Sound("assets/coin.wav").play()
                self.coinSprites.remove(coinSprite)
                self.sprites.remove(coinSprite)
                self.character.player.coins = self.character.player.coins + 1
            
        if pygame.sprite.spritecollideany(self.character, self.enemySprites):
            self.character.player.reset()
            self.switchSceneEvent(EVENT_SCENEGAMEOVER)