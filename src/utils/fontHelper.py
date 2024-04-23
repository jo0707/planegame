
import pygame

fonts_description = {
    "default": {
        "name": "default",
        "size": int(20),
    },
    "pixel": {
        "name": "fonts/pixel.ttf",
        "size": int(20),
    },
}

fonts: dict[str, pygame.font.Font] = {}

def initFonts():
    for font_name, font in fonts_description.items():
        if font_name == "default":
            fonts[font_name] = pygame.font.SysFont("arial", 20, True)
        else:
            fonts[font_name] = pygame.font.Font(font["name"], font["size"])