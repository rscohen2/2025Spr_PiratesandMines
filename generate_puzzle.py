#
# import random
# import numpy as np
#
#
#
#
# class Game:
#     def __init__(self):
#         self.board = [[' ' for _ in range(9)] for _ in range(9)]
#         self.grid_size = (6, 6)
#         self.game_over = False
#
# t = 1
# e = 0
# l = -1
#
# example_board = [['_','_',0],['_',1,'_'],['_',-1,-1]]
#
# example_board_solved = [[t,t,0],[t,1,l],[l,-1,-1]]
#
#
# def is_valid_board_complete(self):
#     """
#     Checks that a completely filled board.
#     """
#     for (i, j) in self.board:
#         if self.grid[i][j] == ' ':
#             return False  # board is not complete
#     return True
#
#
# def generate_solved_puzzle(height, width):
#     """
#     Generates a random Haunted Mirror Maze puzzle of given height and width.
#     The puzzle is created by randomly placing mirrors and then randomly distributing
#     monsters over the remaining cells (to form a complete solution). Clues are computed
#     from that solution. The solver is then used to verify that the puzzle (with monsters
#     removed) has a unique solution. When a unique puzzle is generated, the puzzle
#     (mirrors, clues, and monster counts) is printed to the console and the solution is
#     written to a file named "solution.txt".
#     """
#     attempt = 0
#     while True:
#         attempt += 1
#         # Create an empty grid (all cells start as empty).
#         grid = [[' ' for _ in range(width)] for _ in range(height)]
#
#         # Randomly place treasure/mines
#         nonempty_probability = 0.50
#
#         for i in range(height):
#             for j in range(width):
#                 if random.random() < nonempty_probability:
#                     grid[i][j] = random.choice(['l', 't'])
#
#                 grid_full = [row[:] for row in grid]
#                 # for _ in range(count_G):
#                 #     if positions:
#                 #         i, j = positions.pop()
#                 #         grid_full[i][j] = 'G'
#         return grid
#
#
# # def add_clues_to_puzzle(grid):
# #     #for any empty cell, sum the t and l cells above/below/next to them
# #     grid = np.array(grid)
# #     rows,cols = grid.shape
# #     for x in range(rows):
# #         for y in range(cols):
# #             if grid[x,y] != 'l' or 't':
# #                 cell_right = (x + 1, y)
# #                 cell_left = (x - 1, y)
# #                 cell_above = (x, y + 1)
# #                 cell_below = (x, y - 1)
# #                 cell_clue = grid[cell_right] + grid[cell_left] + gridf[cell_above] + grid[cell_below]
# #                 cell = cell_clue
# #         return grid
#
#
# def get_clues(grid):
#     grid = np.array(grid)
#     rows, cols = grid.shape
#
#     # Function to convert cell values to numbers
#     def cell_value(val):
#         if val == 't':
#             return 1
#         elif val == 'l':
#             return -1
#         try:
#             return int(val)
#         except ValueError:
#             return 0
#
#     for x in range(rows):
#             for y in range(cols):
#                 if grid[x, y] != 'l' and grid[x,y]!= 't':
#                     cell_clue = 0
#                     directions = {
#                     'cell_right': (x+1, y),
#                     'cell_left': (x-1, y),
#                     'cell_above': (x, y+1),
#                     'cell_below': (x, y-1)}
#                     for dir_name, (nx, ny) in directions.items():
#                         if 0 <= nx < rows and 0 <= ny < cols:
#                             neighbor_value = grid[nx, ny]
#                             if neighbor_value != ' ':
#                                 cell_clue += cell_value(neighbor_value)
#                     # cell_clue = grid[cell_right] + grid[cell_left] + grid[cell_above] + grid[cell_below]
#                                 grid[x, y] = cell_clue
#     return grid
#
# #TODO: create the function below in order to have a puzzle to solve
# def remove_aLL_treasure_and_mines(solved_puzzle):
#     rows, cols = solved_puzzle.shape
#     grid = solved_puzzle
#     for x in range(rows):
#             for y in range(cols):
#                 if grid[x, y] == 'l' or grid[x,y] == 't':
#                     grid[x,y] = 'e'
#     return grid
#
#
#
# def generate_unsolved_puzzle(height, width):
#     solved_puzzle = generate_solved_puzzle(height, width)
#     puzzle_clues = get_clues(solved_puzzle)
#     unsolved_puzzle = remove_aLL_treasure_and_mines(puzzle_clues)
#     return unsolved_puzzle
#
#
# #TODO: create func to verify generated puzzle has only 1 solution
# def verify_only_one_soln():
#     def find_solutions(self):
#         """
#         Searches for solutions by filling in all monster cells.
#         If more than one solution is found, the search stops once two have been found.
#         Returns a list of complete grids (each grid is a list of lists).
#         """
#         self.solutions = []
#         self._solve_recursive(0)
#         return self.solutions[:2]  # if more than one solution, returning only two of them
#
#     def _solve_recursive(self, index):
#         # If we already have two solutions, we stop searching.
#         if len(self.solutions) >= 2:
#             return
#
#         if self.is_valid_board_complete():
#             # Save a deep copy of the grid as a solution.
#             sol = [row[:] for row in self.grid]
#             self.solutions.append(sol)
#             return
#
#
#     pass
#
#
#
#
#
# #TODO: make sure the puzzle works for varying sizes, and possibly add difficulties like diaganol cells counting towards the clue etc
#     ##Vedant and Becca?
#
# #TODO: (optional)create an interactive UI to play the project?
#     ##Vedant
#
# #TODO: write the README to be an introduction about our puzzle
#     ##Becca?
#
# #TODO: live class presentation
#     ##Everyone for the parts they coded/worked on
#
# #TODO: targeted algorithm analysis
#     ##Vedant
#
# #TODO: performance measurement
#     ##Ke
#
# #TODO: clean up and document code
#     #Becca
#
#
#
# if __name__ == "__main__":
#     # grid = generate_solved_puzzle(6,6)
#     # grid = solve_puzzle(grid)
#     # print(grid)
#     unsolved_puzzle = generate_unsolved_puzzle(6,6)
#     print(unsolved_puzzle)
#
#
#
#
#


# generate_puzzle.py
import numpy as np
import random
from solver import PuzzleSolver


class PuzzleGenerator:
    def __init__(self, size=6, difficulty='medium'):
        self.size = size
        self.difficulty = difficulty
        self.grid = np.full((size, size), 'e', dtype=object)
        self.clue_grid = np.zeros((size, size), dtype=int)

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
    generator = PuzzleGenerator(size=9, difficulty='medium')
    puzzle, solution = generator.create_puzzle()
    print("Puzzle:")
    print(np.matrix(puzzle))
    print("\nSolution:")
    print(np.matrix(solution))