import numpy as np
import random

class Environment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols)) # 0: Empty, 1: Obstacle
        
    def add_obstacle(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = 1

    def remove_obstacle(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = 0

    def clear(self):
        self.grid.fill(0)

    def generate_random_obstacles(self, density=0.2):
        self.clear()
        for r in range(self.rows):
            for c in range(self.cols):
                if random.random() < density:
                    self.grid[r][c] = 1

    def is_valid_pos(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0
