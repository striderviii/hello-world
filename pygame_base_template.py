
import pygame

pygame.init()

# Defining some colors

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)

PI = 3.141592653

# Set the width and height of the screen [width, height]

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.mouse.set_pos((700/2),(500/2))

def mousePosition():
    return pygame.mouse.get_pos()[1]


pygame.display.set_caption("Professor Craven's Cool Game")

paddleSize =  [15, 50]



def drawPaddle(x, y):
    pygame.draw.rect(screen, BLACK,[x, y, 15, 50])


pos = pygame.mouse.get_pos()
x = pos[0]
y = pos[1]

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the clock screen updates
clock = pygame.time.Clock()

# --------------- Main Program Loop ---------------

while not done:
    #--- Main event loop
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If use clicked close
            done = True # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:
            print("Escape")
            done = True


        if event.type == pygame.MOUSEMOTION:
            if event.rel[1] != 0:
                print('Youre moving the paddle')
                print(mousePosition())
                pos = pygame.mouse.get_pos()
                y = pos[1]






    # Game logic goes here

    # Screen clearing goes here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Drawing logic goes here
    # Draw a rectangle

    drawPaddle(400, y)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    #--- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()


