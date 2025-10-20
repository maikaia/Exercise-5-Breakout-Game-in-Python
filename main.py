import pygame
from pygame.locals import *
import sys
from Ball import * # Import Ball class
from Bat import * # Import Bat class
from Brick import * #Import Brick class

# Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 840
WINDOW_HEIGHT = 680
FRAMES_PER_SECOND = 60

# Initialize Pygame
pygame.init()
# Set up window and clock
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Create Ball instance
ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
bat = Bat(window, WINDOW_WIDTH, WINDOW_HEIGHT)
brick = Brick(window)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update game state
    ball.update(bat, brick, WINDOW_HEIGHT, WINDOW_WIDTH)
    bat.update()

    # Draw everything
    window.fill(BLACK)

    # Draw ball and bat
    ball.draw()
    bat.draw()

    # Draw bricks
    for x in range(10, WINDOW_WIDTH, brick.width + 10):
        for y in range(50, 100, brick.height + 10):
            brick.draw(x, y)

    # Update display and tick clock
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)