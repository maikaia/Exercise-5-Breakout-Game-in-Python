import pygame
from pygame.locals import *
import sys
from Ball import * # Import Ball class
from Bat import * # Import Bat class
from Brick import * #Import Brick class
from random import randint

# Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 890
WINDOW_HEIGHT = 680
FRAMES_PER_SECOND = 60
PAUSE = True
GAMEOVER = False

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
        
        # Pause game on ESC key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                PAUSE = True
    

    if ball.lives <= 0:
        GAMEOVER = True

    if all(not brick.alive for brick in bricks):
        GAMEOVER = True

    if GAMEOVER:
        window.fill(BLACK)
        draw_text("GAME OVER", pygame.font.SysFont(None, 75), (255, 0, 0), window, WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 50)
        draw_text(f"Final Score: {ball.score}", pygame.font.SysFont(None, 55), (255, 255, 255), window, WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 20)
        draw_text("Press SPACE to Restart", pygame.font.SysFont(None, 45), (255, 255, 255), window, WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 80)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            # Reset game state
            ball.lives = 3
            ball.score = 0
            ball.x = WINDOW_WIDTH / 2
            ball.y = WINDOW_HEIGHT / 2
            bat.x = (WINDOW_WIDTH - bat.width) / 2
            bricks = []
            for x in range(10, WINDOW_WIDTH - 100, 110):
                for y in range(50, 150, 30):
                    lives = randint(1, 3)  # Random lives between 1 and 3
                    bricks.append(Brick(window, x, y, lives))
            GAMEOVER = False
            PAUSE = True
            

        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)
        continue

    # If not paused, update game state
    if not PAUSE:
        # Update game state
        bat.update()
        ball.update(bat, bricks)

        # Draw everything
        window.fill(BLACK)
        ball.draw()
        bat.draw()
        for brick in bricks:
            brick.draw()

        # Draw score and lives
        draw_text(f"Score: {ball.score}", pygame.font.SysFont(None, 30), (255, 255, 255), window, 70, 20)
        draw_text(f"Lives: {ball.lives}", pygame.font.SysFont(None, 30), (255, 255, 255), window, WINDOW_WIDTH - 70, 20)

    else:
        draw_text("Press SPACE to Start", pygame.font.SysFont(None, 55), (255, 255, 255), window, WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            PAUSE = False
    
    # Update display and tick clock
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)