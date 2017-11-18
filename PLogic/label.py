import pygame
from PLogic import RenderObject


class Label(RenderObject):
    def __init__(self, text, font, size, pos, color):
        super().__init__()
        self.pos = pos
        self.textsurface = font.render(text, False, color)

    def rect(self):
        pass

    def render(self, viewport, renderer):
        renderer.blit(self.textsurface, self.pos)

    def on_remove(self):
        pass