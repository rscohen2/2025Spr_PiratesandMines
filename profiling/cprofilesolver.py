# solver.py
import numpy as np

class PuzzleSolver:
    def __init__(self, clue_grid, diagonal):
        self.size = len(clue_grid)
        self.clue_grid = np.array(clue_grid)
        self.solution_count = 0
        self.solutions = []
        self.diagonal = False

    def count_solutions(self):
        """Count number of valid solutions"""
        self.solution_count = 0
        self.solutions.clear()
        self._solve(0, 0, np.full((self.size, self.size), '?', dtype=object))
        return self.solution_count

    def _solve(self, row, col, grid):
        """Recursive backtracking solver"""
        if row == self.size:
            if self._validate_solution(grid):
                self.solution_count += 1
                self.solutions.append(grid.copy())
            return

        next_row = row + 1 if col == self.size - 1 else row
        next_col = 0 if col == self.size - 1 else col + 1

        if self.clue_grid[row][col] != '?':
            # Cell with clue - skip
            self._solve(next_row, next_col, grid)
            return

        for value in ['t', 'l']:
            if self._is_valid_placement(row, col, value, grid):
                grid[row][col] = value
                self._solve(next_row, next_col, grid)
                grid[row][col] = '?'  # Backtrack

    def _is_valid_placement(self, row, col, value, grid, diagonal= False):
        """Check if placement maintains validity of all clues"""
        temp_grid = grid.copy()
        temp_grid[row][col] = value
        if not diagonal:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = row + dx, col + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if isinstance(self.clue_grid[nx][ny], (int, np.integer)):
                        expected = self.clue_grid[nx][ny]
                        actual = self._calculate_clue(nx, ny, temp_grid)
                        if actual != expected:
                            return False
            return True
        elif diagonal:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),
                           (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nx, ny = row + dx, col + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if isinstance(self.clue_grid[nx][ny], (int, np.integer)):
                        expected = self.clue_grid[nx][ny]
                        actual = self._calculate_clue(nx, ny, temp_grid)
                        if actual != expected:
                            return False
            return True


    def _calculate_clue(self, x, y, grid, diagonal=False):
        """Calculate clue value for a position"""
        total = 0
        if not diagonal:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if grid[nx][ny] == 't':
                        total += 1
                    elif grid[nx][ny] == 'l':
                        total -= 1
            return total
        elif diagonal:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),
                           (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if grid[nx][ny] == 't':
                        total += 1
                    elif grid[nx][ny] == 'l':
                        total -= 1


    def _validate_solution(self, grid):
        """Validate complete solution"""
        for i in range(self.size):
            for j in range(self.size):
                if isinstance(self.clue_grid[i][j], (int, np.integer)):
                    if self._calculate_clue(i, j, grid) != self.clue_grid[i][j]:
                        return False
        return True

if __name__ == "__main__":
    # Profile solver alone using a sample clue grid
    import cProfile, pstats, io

    # Example: 6x6 empty clue grid
    size = 6
    sample_clues = np.zeros((size, size), dtype=int)
    solver = PuzzleSolver(sample_clues)
    solver_diag = PuzzleSolver(sample_clues, diagonal = True)


    profiler = cProfile.Profile()
    profiler.enable()
    count = solver.count_solutions()
    profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats('cumtime')
    stats.print_stats(10)

    print(f"\nSolver Profiling Summary (top 10 cumulative):")
    print(stream.getvalue())
    print(f"Total solutions found: {count}")