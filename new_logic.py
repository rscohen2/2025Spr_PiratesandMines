import numpy as np
from itertools import product
import unittest


class Grid:
    def __init__(self, size=5):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)  # -1: Landmine, 1: Treasure, 0: Empty (clue)
        self.clues = np.full((size, size), None)  # Sums for empty cells

    def get_neighbors(self, row, col):
        """Get all 8 neighbors (orthogonal + diagonal)."""
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  # Skip self
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    neighbors.append((nr, nc))
        return neighbors

    def calculate_clues(self):
        """Compute clues for empty cells."""
        for i, j in product(range(self.size), repeat=2):
            if self.grid[i, j] == 0:
                neighbors = self.get_neighbors(i, j)
                self.clues[i, j] = sum(self.grid[nr, nc] for (nr, nc) in neighbors)

    def generate_puzzle(self, num_treasures=3, num_mines=3):
        """Generate a puzzle with a unique solution."""
        while True:
            # Reset grid
            self.grid.fill(0)
            indices = np.random.choice(
                self.size * self.size,
                num_treasures + num_mines,
                replace=False
            )
            # Place treasures
            for i in indices[:num_treasures]:
                row, col = i // self.size, i % self.size
                self.grid[row, col] = 1
            # Place landmines
            for i in indices[num_treasures:]:
                row, col = i // self.size, i % self.size
                self.grid[row, col] = -1
            # Compute clues and validate
            self.calculate_clues()
            if self.validate_unique():
                break

    def validate_unique(self):
        """Check if the puzzle has exactly one solution."""
        return self.count_solutions() == 1

    def count_solutions(self):
        """Backtracking solver to count valid solutions."""
        clue_cells = []
        variable_cells = []
        for i, j in product(range(self.size), repeat=2):
            if self.grid[i, j] == 0:
                clue_cells.append((i, j, self.clues[i, j]))
            else:
                variable_cells.append((i, j))

        solution_count = 0
        solver_grid = np.zeros((self.size, self.size), dtype=int)

        def backtrack(idx):
            nonlocal solution_count
            if idx == len(variable_cells):
                # Validate all clues
                valid = True
                for i, j, clue in clue_cells:
                    neighbors = self.get_neighbors(i, j)
                    total = sum(solver_grid[nr, nc] for (nr, nc) in neighbors)
                    if total != clue:
                        valid = False
                        break
                if valid:
                    solution_count += 1
                return

            r, c = variable_cells[idx]
            for val in [1, -1]:
                solver_grid[r, c] = val
                backtrack(idx + 1)
                solver_grid[r, c] = 0  # Reset

        backtrack(0)
        return solution_count

    def solve(self):
        """Return the unique solution grid."""
        clue_cells = [(i, j, self.clues[i, j])
                      for i, j in product(range(self.size), repeat=2)
                      if self.grid[i, j] == 0]
        variable_cells = [(i, j)
                          for i, j in product(range(self.size), repeat=2)
                          if self.grid[i, j] != 0]

        solution = None
        solver_grid = np.zeros((self.size, self.size), dtype=int)

        def backtrack(idx):
            nonlocal solution
            if solution is not None:
                return  # Early exit
            if idx == len(variable_cells):
                valid = True
                for i, j, clue in clue_cells:
                    neighbors = self.get_neighbors(i, j)
                    total = sum(solver_grid[nr, nc] for (nr, nc) in neighbors)
                    if total != clue:
                        valid = False
                        break
                if valid:
                    solution = solver_grid.copy()
                return

            r, c = variable_cells[idx]
            for val in [1, -1]:
                solver_grid[r, c] = val
                backtrack(idx + 1)
                solver_grid[r, c] = 0

        backtrack(0)
        return solution


# class TestTreasureMine(unittest.TestCase):
#     def test_unique_solution(self):
#         """Verify generated puzzles have exactly one solution."""
#         grid = Grid(size=3)
#         grid.generate_puzzle(num_treasures=2, num_mines=2)
#         self.assertEqual(grid.count_solutions(), 1)
#
#     def test_solver_accuracy(self):
#         """Verify solver matches original solution."""
#         grid = Grid(size=3)
#         grid.generate_puzzle(num_treasures=2, num_mines=2)
#         solution = grid.solve()
#         # Compare solver's solution with original grid
#         for i, j in product(range(3), repeat=2):
#             if grid.grid[i, j] != 0:  # Only check variable cells
#                 self.assertEqual(solution[i, j], grid.grid[i, j])


if __name__ == "__main__":
    grid = Grid(size=8)
    grid.generate_puzzle(num_treasures=4, num_mines=7)
    print("Clues:\n", grid.clues)
    print("Solution:\n", grid.solve())