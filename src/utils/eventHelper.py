import pygame

EVENT_COUNT = 0

def newEvent():
    global EVENT_COUNT
    EVENT_COUNT = EVENT_COUNT + 1
    return pygame.USEREVENT + EVENT_COUNT

EVENT_NEWENEMY = newEvent()
EVENT_NEWCOIN = newEvent()
EVENT_SCENESTART = newEvent()