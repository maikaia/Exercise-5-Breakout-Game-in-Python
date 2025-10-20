import pygame
from pygame.locals import *

# Brick class
class Brick():
    def __init__(self, window):
        self.window = window
        # self.x = x
        # self.y = y
        self.width = 100
        self.height = 10
        self.color = (255, 0, 0)
        self.lives = 1

    def draw(self, x, y):
        pygame.draw.rect(self.window, self.color, pygame.Rect(x, y, self.width, self.height))

    def hit(self):
        self.lives -= 1
        self.color = (0, 0, 255)