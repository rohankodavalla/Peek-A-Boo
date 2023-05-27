import random

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [['X' for _ in range(size)] for _ in range(size)]
        self.pairs = self.generate_pairs()

    def generate_pairs(self):
        total_pairs = self.size * self.size // 2
        numbers = list(range(total_pairs)) * 2
        random.shuffle(numbers)
        pairs = [numbers[i:i+2] for i in range(0, total_pairs*2, 2)]
        return pairs

    def reveal_cell(self, row, col):
        self.grid[row][col] = str(self.pairs[row][col])

    def hide_cell(self, row, col):
        self.grid[row][col] = 'X'

    def is_cell_revealed(self, row, col):
        return self.grid[row][col] != 'X'

    def is_grid_full(self):
        for row in self.grid:
            if 'X' in row:
                return False
        return True

    def get_cell(self, row, col):
        return self.grid[row][col]

    def get_pairs(self):
        return self.pairs

    def get_size(self):
        return self.size

    