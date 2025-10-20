import pygame
from pygame.locals import *
import sys
from Ball import * # Import Ball class
from Bat import * # Import Bat class

# Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 840
WINDOW_HEIGHT = 680
FRAMES_PER_SECOND = 60
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
# Set up window and clock
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Create Ball instance
ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
bat = Bat(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update game state
    ball.update(bat)
    bat.update()

    # Draw everything
    window.fill(BLACK)

    # Draw ball and bat
    ball.draw()
    bat.draw()

    # Update display and tick clock
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)