import pygame
from pygame.locals import *

# Bat class
class Bat():
    def __init__(self, window, windowWidth, windowHeight):
        self.x = windowWidth / 2
        self.y = windowHeight - 30
        self.color = (255, 255, 255)
        self.width = 150
        self.height = 20
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def move_left(self, distance):
        self.x = max(0, self.x - distance)

    def move_right(self, distance, windowWidth):
        self.x = min(windowWidth - self.width, self.x + distance)
        
    # Update the bat's position
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left(10)
        if keys[pygame.K_RIGHT]:
            self.move_right(10, self.window.get_width())