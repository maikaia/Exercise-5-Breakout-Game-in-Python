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
FRAMES_PER_SECOND = 120
PAUSE = True

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

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    surface.blit(textobj, (x - textobj.get_width() // 2, y - textobj.get_height() // 2))

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # If not paused, update game state
    if not PAUSE:
        # Update game state
        bat.update()
        ball.update(bat, bricks)

        # Draw everything
        window.fill(BLACK)
        draw_text("Points: 0".format(sum(3 - brick.lives for brick in bricks if not brick.alive)), pygame.font.SysFont(None, 30), (255, 255, 255), window, 70, 20)
        draw_text("Lives: 3", pygame.font.SysFont(None, 30), (255, 255, 255), window, WINDOW_WIDTH - 70, 20)
        ball.draw()
        bat.draw()
        for brick in bricks:
            brick.draw()

    else:
        draw_text("Press SPACE to Start", pygame.font.SysFont(None, 55), (255, 255, 255), window, WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            PAUSE = False
    
    # Update display and tick clock
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)