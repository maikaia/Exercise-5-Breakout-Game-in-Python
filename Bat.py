import pygame
from pygame.locals import *
from Sprite import Sprite

class Bat(Sprite):
    def __init__(self, window, windowWidth, windowHeight):
        # Define bat’s size and starting position
        self.width = 100
        self.height = 10
        self.x = (windowWidth - self.width) / 2
        self.y = windowHeight - 50
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.speed = 6

        # Call Sprite superclass to initialize shared attributes
        super().__init__(window, self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 255), (self.x, self.y, self.width, self.height))

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