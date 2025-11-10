import pygame
from pygame.locals import *

# Brick class
class Brick():
    def __init__(self, window, x, y, lives):
        self.window = window
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        self.lives = lives
        self.alive = True
        self.colors = {
            3: (255, 0, 0),     # Red = strong
            2: (255, 165, 0),   # Orange = medium
            1: (255, 255, 0),   # Yellow = weak
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
