import pygame
from pygame.locals import *
import random

# Ball class
class Ball():
    # Initialize ball
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth 
        self.windowHeight= windowHeight

        self.image = pygame.image.load('images/ball.png').convert_alpha()

        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        self.x = self.maxWidth/2
        self.y = self.maxHeight/2

        self.xSpeed = 4
        self.ySpeed = 4

    # Update ball position
    def update(self):
        if(self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        if(self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    # Draw ball on window
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

