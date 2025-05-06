
import numpy as np


class PuzzleSolver:
    def __init__(self, clue_grid, diagonal = False):
        self.size = len(clue_grid)
        self.clue_grid = np.array(clue_grid)
        self.solution_count = 0
        self.solutions = []
        self.diagonal = diagonal

    def count_solutions(self):
        """Count number of valid solutions"""

        #TODO: tried changing this to ? to see if that is why solution was all es before
        grid =  np.full((self.size, self.size), '?')

        # Copy clues into working grid
        for row in range(self.size):
            for col in range(self.size):
                if self.clue_grid[row][col] != 'e':
                    grid[row][col] = self.clue_grid[row][col]
                else:
                    continue
        solution = self._solve(0,0,grid)
        # self._solve(0, 0, np.full((self.size, self.size), 'e'))
        return self.solution_count

    def _solve(self, row, col, grid):
        """Recursive backtracking solver"""
        if row == self.size:
            if self._validate_solution(grid):
                self.solution_count += 1
                self.solutions.append(grid.copy())
            return

        next_row = row + 1 if col == self.size - 1 else row
        next_col = col + 1 if col < self.size - 1 else 0

        if self.clue_grid[row][col] != 'e':
            # Cell with clue - skip
            self._solve(next_row, next_col, grid)
            return

        # Try both possibilities
        for value in ['t', 'l']:
            if self._is_valid_placement(row, col, value, grid, self.diagonal):
                grid[row][col] = value
                self._solve(next_row, next_col, grid)
            if not self._validate_solution(grid):

                grid[row][col] = '?'  # Backtrack

    def _is_valid_placement(self, row, col, value, grid, diagonal):
        """Check if placement maintains validity of all clues"""
        # temp_grid = grid.copy()
        # temp_grid[row][col] = value
        original = grid[row][col]  # Save current value
        grid[row][col] = value  # Temporarily place the value

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        # Add diagonals if enabled
        if diagonal:
            directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
                nx, ny = row + dx, col + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if isinstance(self.clue_grid[nx][ny], int):
                        expected = self.clue_grid[nx][ny]
                        actual = self._calculate_clue(nx, ny, temp_grid)
                        if actual != expected:
                            grid[row][col] = original  # Restore original value
                            return False
                grid[row][col] = original
                return True


    def _calculate_clue(self, x, y, grid, diagonal):
        """Calculate clue value for a position"""
        total = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        # Add diagonals if enabled
        if diagonal:
            directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if self.grid[nx][ny] == 't':
                    total += 1
                elif self.grid[nx][ny] == 'l':
                    total -= 1
            return total


    def _validate_solution(self, grid):
        """Validate complete solution"""
        for i in range(self.size):
            for j in range(self.size):
                if isinstance(self.clue_grid[i][j], int):
                    if self._calculate_clue(i, j, grid) != self.clue_grid[i][j]:
                        return False
        return True
