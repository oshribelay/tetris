import pygame
import random
from consts import *


class Tetromino:
    def __init__(self):
        self.shape = random.choice(TETROMINOES)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def move_right(self):
        self.x += 0.2

    def move_left(self):
        self.x -= 0.2

    def move_down(self):
        self.y += 0.2

    def rotate(self):
        # Implement tetromino rotation
        pass

    def draw(self, screen):
        for row_index, row in enumerate(self.shape):
            for column_index, cell in enumerate(row):
                if cell == 1:
                    pygame.draw.rect(
                        screen,
                        WHITE,
                        (
                            (self.x + column_index) * CELL_SIZE,
                            (self.y + row_index) * CELL_SIZE,
                            CELL_SIZE,
                            CELL_SIZE,
                        ),
                    )
