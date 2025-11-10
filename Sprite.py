import pygame

class Sprite:
    def __init__(self, window, x, y, width, height):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        raise NotImplementedError("Subclasses must implement draw().")
