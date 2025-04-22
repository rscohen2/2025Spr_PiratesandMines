

# Generate a puzzle
generator = PuzzleGenerator(size=6, difficulty='medium')
puzzle, solution = generator.create_puzzle()

# Solve a puzzle
solver = PuzzleSolver(puzzle)
if solver.count_solutions() == 1:
    print("Unique solution:", solver.solutions[0])