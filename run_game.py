from generate_puzzle_orig import PuzzleGenerator
import numpy as np


if __name__ == "__main__":
    grid_size = int(input("Enter the grid size (n x n): "))
    difficulty = input("Enter the difficulty (easy, medium, hard): ").lower()
    generator = PuzzleGenerator(size = grid_size, difficulty = difficulty)
    puzzle, solution = generator.create_puzzle()
    print("Puzzle:")
    print(np.matrix(puzzle))
    # print("\nSolution:")
    # print(np.matrix(solution))