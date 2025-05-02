# generate_puzzle.py
import numpy as np
import random
import cProfile
import pstats
import io
from solver import PuzzleSolver

class PuzzleGenerator:
    def __init__(self, size=6, difficulty='medium', diagonal = False):
        self.size = size
        self.difficulty = difficulty
        self.grid = np.full((size, size), 'e', dtype=object)
        self.clue_grid = np.zeros((size, size), dtype=int)
        self.diagonal = diagonal

        # Difficulty settings
        self.difficulty_params = {
            'easy': {'mine_prob': 0.2, 'treasure_prob': 0.3},
            'medium': {'mine_prob': 0.3, 'treasure_prob': 0.2},
            'hard': {'mine_prob': 0.4, 'treasure_prob': 0.1}
        }

    def generate_valid_solution(self):
        """Generates a valid puzzle solution with treasures and mines"""
        params = self.difficulty_params[self.difficulty]
        for i in range(self.size):
            for j in range(self.size):
                rand = random.random()
                if rand < params['mine_prob']:
                    self.grid[i][j] = 'l'
                elif rand < params['mine_prob'] + params['treasure_prob']:
                    self.grid[i][j] = 't'
                else:
                    self.grid[i][j] = 'e'

        # Calculate initial clues
        self._calculate_clues()

        # Verify uniqueness
        solver = PuzzleSolver(self.clue_grid)
        if solver.count_solutions() == 1:
            return self.grid, self.clue_grid
        return self.generate_valid_solution()  # Retry if not unique

    def _calculate_clues(self):
        """Calculate clue values for empty cells"""
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 'e':
                    self.clue_grid[i][j] = self._get_neighbor_sum(i, j)
                else:
                    self.clue_grid[i][j] = 0  # Non-clue cells

    def _get_neighbor_sum(self, x, y):
        """Calculate sum of orthogonal neighbors"""
        total = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if self.grid[nx][ny] == 't':
                    total += 1
                elif self.grid[nx][ny] == 'l':
                    total -= 1
        return total

    def create_puzzle(self):
        """Create the final puzzle matrix"""
        solution, clues = self.generate_valid_solution()
        puzzle = np.where(solution == 'e', clues, '?')
        return puzzle.tolist(), solution.tolist()

if __name__ == "__main__":
    # Profile puzzle generation and solver
    profiler = cProfile.Profile()
    profiler.enable()

    generator = PuzzleGenerator(size=9, difficulty='medium')
    puzzle, solution = generator.create_puzzle()

    profiler.disable()
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats('cumtime')
    stats.print_stats(10)

    print("\nProfiling Summary (Puzzle + Solver count_solutions):")
    print(stream.getvalue())

    print("Puzzle:")
    print(np.matrix(puzzle))
    print("\nSolution:")
    print(np.matrix(solution))