import pygame
from pygame.locals import *
from Sprite import Sprite

# Ball class
class Ball(Sprite):
    # Initialize ball
    def __init__(self, window, windowWidth, windowHeight):
        # Load ball image
        self.image = pygame.image.load('images/ball.png').convert_alpha()
        ballRect = self.image.get_rect()

        # Call Sprite's __init__ to set x, y, width, height
        super().__init__(window, windowWidth/2, windowHeight/2, ballRect.width, ballRect.height)

        # Variables
        self.windowWidth = windowWidth 
        self.windowHeight = windowHeight
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        self.xSpeed = 4
        self.ySpeed = 4
        self.lives = 3
        self.score = 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    # Update ball position
    def update(self, bat, bricks):
        # Bounce ball off side walls
        if self.x < 0 or self.x >= self.maxWidth:
            self.xSpeed = -self.xSpeed

        # Bounce ball off bat or top wall
        if(self.y + self.height >= bat.y) and (bat.x <= self.x + self.width/2 <= bat.x + bat.width) or (self.y < 0):
            self.ySpeed = -self.ySpeed

        # Resets ball if it goes below screen
        if self.y > self.maxHeight + self.height:
            pygame.time.delay(1000)
            self.x = self.maxWidth/2
            self.y = self.maxHeight/2
            self.lives -= 1

        # Bounce ball off bricks
        ball_rect = self.get_rect()
        for brick in bricks:
            if brick.alive:
                brick_rect = pygame.Rect(brick.x, brick.y, brick.width, brick.height)
                if ball_rect.colliderect(brick_rect):
                    # Determine bounce direction
                    if abs(brick_rect.top - ball_rect.bottom) < 10 and self.ySpeed > 0:
                        self.ySpeed = -self.ySpeed  # Hit top of brick
                    elif abs(brick_rect.bottom - ball_rect.top) < 10 and self.ySpeed < 0:
                        self.ySpeed = -self.ySpeed  # Hit bottom of brick
                    elif abs(brick_rect.left - ball_rect.right) < 10 and self.xSpeed > 0:
                        self.xSpeed = -self.xSpeed  # Hit left side
                    elif abs(brick_rect.right - ball_rect.left) < 10 and self.xSpeed < 0:
                        self.xSpeed = -self.xSpeed  # Hit right side

                    brick.hit()
                    self.score += 10 + 10 * brick.lives # 10 points for yellow, 20 for orange, 30 for red
                    break  # Stop after one collision

        # Update ball position
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    # Draw ball on window
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

