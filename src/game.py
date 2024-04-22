import pygame

from src.services.scenemanager import SceneManager
from src.utils.fontHelper import initFonts
from src.utils.eventHelper import EVENT_SCENESTART

"""Game class defines global variables and game loop
"""

class Game:
    SCREEN_WIDTH=1000
    SCREEN_HEIGHT=800
    FPS=144
    WINDOW_TITLE="Plane Game"
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()
    running = True
    
    def __init__(self):
        pygame.init()
        initFonts()
        self.sceneManager = SceneManager(Game.screen)
        
    def onEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or not Game.running:
                self.endGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sceneManager.onClick(event.pos)
            if event.type == EVENT_SCENESTART:
                print("Game started")
                
                
    def gameLoop(self):
        while Game.running:
            self.onEvents()
            self.sceneManager.onTick()
            pygame.display.flip()
            Game.clock.tick(Game.FPS)

    def endGame(self):
        pygame.quit()