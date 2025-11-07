import pygame
from pygame.locals import *
import sys
from Ball import * # Import Ball class
from Bat import * # Import Bat class
from Brick import * #Import Brick class
from random import randint

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

# Create a list of bricks
bricks = []
for x in range(10, WINDOW_WIDTH - 100, 110):
    for y in range(50, 150, 30):
        lives = randint(1, 3)  # Random lives between 1 and 3
        bricks.append(Brick(window, x, y, lives))

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update game state
    bat.update()
    ball.update(bat, bricks)

    # Draw everything
    window.fill(BLACK)
    ball.draw()
    bat.draw()
    for brick in bricks:
        brick.draw()

    # Update display and tick clock
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)