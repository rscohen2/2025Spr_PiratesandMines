from solver_orig import PuzzleSolver
from generate_puzzle_orig import PuzzleGenerator

# Generate a puzzle
if __name__ == "__main__":
    generator = PuzzleGenerator(size=7, difficulty='medium')
    puzzle, solution = generator.create_puzzle()

    # Solve a puzzle
    solver = PuzzleSolver(puzzle)
    if solver.count_solutions() == 1:
        print("Unique solution:", solver.solutions[0])