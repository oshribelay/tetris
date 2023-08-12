import pygame
from consts import *
from tetrominos import Tetromino

# initialize pygame module
pygame.init()

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

# define the game grid
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# initialize the tetromino
tetromino = Tetromino()

# start the game loop
clock = pygame.time.Clock()
run = True
while run:

    screen.fill(BLACK)  # reset the screen to black

    # Draw the grid
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col] == 1:
                # Draw a filled rectangle for each cell containing a block
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                # Draw an empty rectangle for empty cells
                pygame.draw.rect(screen, GRAY, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    # draw the tetromino
    tetromino.draw(screen)

    key = pygame.key.get_pressed()  # gets the pressed key similar to the on keydown event listener

    # capture key press events and move tetromino respectively
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        tetromino.move_left()
    elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        tetromino.move_right()
    elif key[pygame.K_s] or key[pygame.K_DOWN]:
        tetromino.move_down()

    for event in pygame.event.get():  # gets all the events from the event listener
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()  # will update the display with the changes that were made in the loop
    clock.tick(30)

pygame.quit()
