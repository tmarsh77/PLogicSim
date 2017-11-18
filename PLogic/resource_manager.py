import pygame


class ResourceManager():
    def __init__(self, path):
        self.path = path

    def load_image(self, path):
        return pygame.image.load(self.path + path)
