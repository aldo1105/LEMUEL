import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1080
screen_height = 608
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Multiple Key Presses Example")

# Pics
image = pygame.image.load('CRacK/backround1.png')
player1_image = pygame.image.load('CRacK/player1.png')
player2_image = pygame.image.load('CRacK/player2.png')

def backround(image):
    size = pygame.transform.scale(image, (1080,608))
    screen.blit(size, (0,0))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Resize player images
player1_image = pygame.transform.scale(player1_image, (50, 88))
player2_image = pygame.transform.scale(player2_image, (50, 88))

# Player1
player1 = player1_image.get_rect()
player1.center = (screen_width // 4, screen_height // 2)
player1_speed = 5
player1_size = 20
player1_direction = "right"

# Player2
player2 = player2_image.get_rect()
player2.center = (3 * screen_width // 4, screen_height // 2)
player2_speed = 5
player2_size = 20
player2_direction = "left"

# Jumping mechanism
jumping1 = False
Y_GRAVITY1 = 1
JUMP_HEIGHT1 = 15
Y_VELOCITY1 = JUMP_HEIGHT1
jumping2 = False
Y_GRAVITY2 = 1
JUMP_HEIGHT2 = 15
Y_VELOCITY2 = JUMP_HEIGHT2

#Starting point
player1.x = 1
player2.x = 1030
# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update player1 position based on keys pressed
    if keys[pygame.K_a]:
        if player1.left > 0:  # Check if the player is not colliding with the left boundary
            player1.x -= player1_speed
            player1_direction = "left"
    if keys[pygame.K_d]:
        if player1.right < screen_width:  # Check if the player is not colliding with the right boundary
            player1.x += player1_speed
            player1_direction = "right"
    if keys[pygame.K_w]:
        jumping1 = True
    if jumping1:
        player1.y -= Y_VELOCITY1
        Y_VELOCITY1 -= Y_GRAVITY1
    if Y_VELOCITY1 < -JUMP_HEIGHT1:
        jumping1 = False
        Y_VELOCITY1 = JUMP_HEIGHT1

    # Update player2 position based on keys pressed
    if keys[pygame.K_LEFT]:
        if player2.left > 0:  # Check if the player is not colliding with the left boundary
            player2.x -= player2_speed
            player2_direction = "left"
    if keys[pygame.K_RIGHT]:
        if player2.right < screen_width:  # Check if the player is not colliding with the right boundary
            player2.x += player2_speed
            player2_direction = "right"
    if keys[pygame.K_UP]:
        jumping2 = True
    if jumping2:
        player2.y -= Y_VELOCITY2
        Y_VELOCITY2 -= Y_GRAVITY2
    if Y_VELOCITY2 < -JUMP_HEIGHT2:
        jumping2 = False
        Y_VELOCITY2 = JUMP_HEIGHT2

    # Draw
    screen.fill(WHITE)
    backround(image)

    # Blit player1 image
    if player1_direction == "left":
        screen.blit(pygame.transform.flip(player1_image, True, False), player1)
    else:
        screen.blit(player1_image, player1)

    # Blit player2 image
    if player2_direction == "left":
        screen.blit(pygame.transform.flip(player2_image, True, False), player2)
    else:
        screen.blit(player2_image, player2)

    pygame.display.flip()

    # Limit frames per second
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
w