import pygame
from pygame.locals import *
from Sprite import Sprite

class Brick(Sprite):
    def __init__(self, window, x, y, lives):
        self.width = 100
        self.height = 20

        # Call the Sprite superclass to handle shared setup
        super().__init__(window, x, y, self.width, self.height)

        self.lives = lives
        self.alive = True
        self.colors = {
            3: (255, 0, 0),
            2: (255, 165, 0),
            1: (255, 255, 0)
        }

    def draw(self):
        if self.alive:
            color = self.colors.get(self.lives, (0, 0, 0))
            pygame.draw.rect(self.window, color, (self.x, self.y, self.width, self.height))

    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            self.alive = False
        else:
            self.color = (0, 0, 255)
