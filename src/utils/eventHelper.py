import pygame

EVENT_COUNT = 0

def newEvent():
    global EVENT_COUNT
    EVENT_COUNT = EVENT_COUNT + 1
    return pygame.USEREVENT + EVENT_COUNT

def postEvent(event: int):
    pygame.event.post(pygame.event.Event(event))

EVENT_NEWENEMY = newEvent()
EVENT_NEWCOIN = newEvent()
EVENT_SCENESTART = newEvent()