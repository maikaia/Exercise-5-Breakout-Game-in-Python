import pygame
from pygame.locals import *
import sys
from Ball import * # import Ball class

# Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 840
WINDOW_HEIGHT = 680
FRAMES_PER_SECOND = 30

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Create Ball instance
ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ball.update()
    window.fill(BLACK)
    ball.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)