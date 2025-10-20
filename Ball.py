import pygame
from pygame.locals import *
from Bat import *  # Import Bat class

# Ball class
class Ball():
    # Initialize ball
    def __init__(self, window, windowWidth, windowHeight):
        # Set window and dimensions
        self.window = window
        self.windowWidth = windowWidth 
        self.windowHeight= windowHeight

        # Load ball image
        self.image = pygame.image.load('images/ball.png').convert_alpha()

        # Get ball dimensions
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height

        # Set max positions
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # Start ball in center of window
        self.x = self.maxWidth/2
        self.y = self.maxHeight/2

        # Set ball speed
        self.xSpeed = 4
        self.ySpeed = 4

    # Update ball position
    def update(self, bat):
        # Bounce ball off side walls
        if(self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        # Bounce ball off bat or top wall
        if(self.y + self.height >= bat.y) and (bat.x <= self.x + self.width/2 <= bat.x + bat.width) or (self.y < 0):
            self.ySpeed = -self.ySpeed

        # Resets ball if it goes below the window
        if(self.y > self.maxHeight+self.height):
            pygame.time.delay(1000)
            self.x = self.maxWidth/2
            self.y = self.maxHeight/2

        # Update ball position
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    # Draw ball on window
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

