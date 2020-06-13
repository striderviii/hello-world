import pygame

pygame.init()

# Defining some colors

Black = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)

PI = 3.141592653

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")


# Loop until the user clicks the close button.
done == False

# Used to manage how fast the clock screen updates
clock = pygame.time.Clock()

# --------------- Main Program Loop ---------------

while not done:
    #--- Main even loop
    for event in pygame.even.get(): # User did something
        if event.type == pygame.Quit: # If use clicked close
            done = True # Flag that we are done so we exit this loop

    # Game logic goes here

    # Drawing logic goes here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    #--- Limit to 60 frames per second
    clock.tick(60)

