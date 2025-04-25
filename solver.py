# from itertools import permutations
#
# from generate_puzzle import generate_unsolved_puzzle
# from generate_puzzle import get_clues
# import numpy as np
# import random
#
# class Game:
#     def __init__(self):
#         self.board = [[' ' for _ in range(6)] for _ in range(6)]
#         self.grid_size = (6, 6)
#         self.game_over = False
#
# t = 1
# e = 0
# l = -1
#
# example_board = [['','_',0],['_',1,'_'],['_',-1,-1]]
#
# example_board_solved = [[t,t,0],[t,1,l],[l,-1,-1]]
#
#
# # Function to convert cell values to numbers
# def cell_value(val):
#     if val == 't':
#         return 1
#     elif val == 'l':
#         return -1
#     try:
#         return int(val)
#     except ValueError:
#         return 0
#
#
# def get_clue(x,y, grid, clue_grid):
#     grid = np.array(grid)
#     rows, cols = grid.shape
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] != 'l' and grid[x, y] != 't':
#                 cell_clue = 0
#                 empty_neighbors_count = 0
#                 directions = {
#                     'cell_right': (x + 1, y),
#                     'cell_left': (x - 1, y),
#                     'cell_above': (x, y + 1),
#                     'cell_below': (x, y - 1)}
#                 for dir_name, (nx, ny) in directions.items():
#                     if 0 <= nx < rows and 0 <= ny < cols:
#                         neighbor_value = grid[nx, ny]
#                         if neighbor_value != 'e':
#                             cell_clue += cell_value(neighbor_value)
#                         else:
#                             empty_neighbors_count += 1
#                 return cell_clue,clue_grid, empty_neighbors_count
#
# def check_clue(cell_clue, clue_grid, empty_neighbors_count,x, y):
#     if cell_clue == clue_grid[x, y]:
#         return True
#         # if cell_clue + 1*empty_neighbors_count or cell_clue -1*empty_neighbors_count == clue_grid[x, y]:
#         #     return True
#     if empty_neighbors_count > 0:
#         permutation_list = generate_all_permutations(empty_neighbors_count)
#         for permutation in permutation_list:
#
#             if cell_clue + permutation[0] == clue_grid[x, y]:
#                 #TODO: add checking of all possible permutations rather than just checking one
#                 #change permutation function to listing all possible permutations?
#                 return True
#     else:
#         if cell_clue == clue_grid[x, y]:
#             return True
#     return False
#
#
#
# # def generate_permutation(n):
# #     # Choose how many -1s and 1s you want (e.g., equal split)
# #     half = n // 2
# #     remainder = n % 2
# #
# #     values = [-1] * half + [1] * half
# #
# #     if remainder:  # If n is odd, add one more randomly
# #         values.append(random.choice([-1, 1]))
# #
# #     random.shuffle(values)  # Shuffle to get a random permutation
# #     return values
#
# def generate_all_permutations(n):
#     half = n // 2
#     remainder = n % 2
#
#     values = [-1] * half + [1] * half
#     if remainder:
#         values.append(1)  # or -1, doesn't matter—both will be included over all perms
#
#     # Use set to avoid duplicates
#     all_perms = set(permutations(values))
#     return list(all_perms)
#
# # # Example usage
# # permutation = generate_permutation(7)
# # print(permutation)
#
#
# def brute_force(grid, puzzle):
#     grid = np.array(grid)
#     rows, cols = grid.shape
#
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x, y] == 'e':
#                 grid[x][y] = 't'
#                 #TODO resolve this function structure/organization
#                 cell_clue, clue_grid, empty_neighbors_count = get_clue(x, y, grid, puzzle)
#                 if check_clue(cell_clue, clue_grid, empty_neighbors_count,x, y):
#                     continue
#                 else:
#                     grid[x][y] = 'l'
#                     # if check_clue(x, y, grid, puzzle):
#                     if check_clue(cell_clue, clue_grid, empty_neighbors_count, x, y):
#
#                         continue
#                     else:
#                         # break
#                         # for i,j in grid where grid[x-i, y-j] == 'l'
#                         for i in range(len(grid)):
#                             for j in range(len(grid[0])):
#                                 xi, yj = x - i, y - j
#                                 if 0 <= xi < len(grid) and 0 <= yj < len(grid[0]):  # bounds check
#                                     if grid[xi][yj] == 'l':
#                                         grid[xi][yj] = 't'
#                                     if grid[xi][yj] == 't':
#                                         grid[xi][yj] = 'l'
#                                 if check_clue(cell_clue, puzzle, empty_neighbors_count, xi, yj):
#                                    # check_clue(cell_clue, clue_grid, empty_neighbors_count, x, y):
#                                     continue
#                                 if check_board_full(grid):
#                                     if validate_entire_grid(grid, puzzle):
#                                         return grid
#                                 else:
#                                     continue
#
#
# def check_board_full(grid):
#     grid = np.array(grid)
#     rows, cols = grid.shape
#     for x in range(rows):
#         for y in range(cols):
#             if grid[x][y] == 'e':
#                 return False
#     return True
#
#
#
#
#
#
#
#     #all permutations that might possibly work
#     #predictable/simple sequence to try, so that any backtracking is as simple as possible also
#     #if layout not valid at all reject the whole thing, if not possible to get that clue
#     #if all empties and middle piece less than 4, then 2 must be treasure and 2 must be landmines etc
#     #or use it to shortcut some of the brute force combinations
#     #if all three full, might deduct last one
#     #backtrack to look for any other soln
#     #erase Ls until last T so becomes L and doesnt work, keep backtracking
#     #backtrack all the way back to beginning, flip to last choice and breaks, cut off half the entire search spoace right away
#     #not is it correct, but a contradiction/any clue that isn't possible with that configuration
#
#     #example code for dominosa, didn't fill the entire thing before
#
#     #could generate combos with multiple solns
#
#
#     # for x in range(rows):
#     #     for y in range(cols):
#     #         if grid[x, y] == 'e':
#     #             grid[x][y] = 't'
#     #         # if grid[x, y] == 'e':
#     #         #         grid[x, y] = 't'
#     # for x in range(rows):
#     #     for y in range(cols):
#     #         if grid[x][y] == 't' or grid[x][y] == 'l':
#     #             if check_clue(x, y, grid, puzzle):
#     #                 # break
#     #                 continue
#     #                     # backtrack
#     #             else:
#     #                 grid[x,y] = 'l'
#     #                 if check_clue(x, y, grid, puzzle):
#     #                     continue
#     #                 else:
#     #                     grid[x, y] = 'e'
#     # return grid
#
#
#
# def validate_entire_grid(grid, puzzle):
#     rows, cols = grid.shape
#     for x in range(rows):
#         for y in range(cols):
#             cell_clue, clue_grid, empty_neighbors_count = get_clue(x, y, grid, puzzle)
#             if not check_clue(cell_clue, puzzle, empty_neighbors_count, x, y):
#                 return False
#     return True
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     game = Game()
#     puzzle = generate_unsolved_puzzle(6,6)
#     solution = puzzle.copy()
#     potential_solution = brute_force(puzzle, solution)
#     print(potential_solution)
#
#
#


# solver.py
import numpy as np

from run import generator
from generate_puzzle_orig import PuzzleGenerator


class PuzzleSolver:
    def __init__(self, clue_grid):
        self.size = len(clue_grid)
        self.clue_grid = np.array(clue_grid)
        self.solution_count = 0
        self.solutions = []

    def count_solutions(self):
        """Count number of valid solutions"""
        self._solve(0, 0, np.full((self.size, self.size), 'e'))
        return self.solution_count

    def solve(self, row, col, grid):
        """Recursive backtracking solver"""
        if row == self.size:
            if self._validate_solution(grid):
                self.solution_count += 1
                self.solutions.append(grid.copy())
            return self.solutions


        next_row = row + 1 if col == self.size - 1 else row
        next_col = col + 1 if col < self.size - 1 else 0

        if self.clue_grid[row][col] != '?':
            # Cell with clue - skip
            self.solve(next_row, next_col, grid)
            return

        # Try both possibilities
        for value in ['t', 'l']:
            if self._is_valid_placement(row, col, value, grid):
                grid[row][col] = value
                self.solve(next_row, next_col, grid)
                grid[row][col] = '?'  # Backtrack

    def _is_valid_placement(self, row, col, value, grid):
        """Check if placement maintains validity of all clues"""
        temp_grid = grid.copy()
        temp_grid[row][col] = value

        # Check all adjacent clues
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = row + dx, col + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if isinstance(self.clue_grid[nx][ny], int):
                    expected = self.clue_grid[nx][ny]
                    actual = self._calculate_clue(nx, ny, temp_grid)
                    if actual > expected or actual < expected:
                        return False
        return True

    def _calculate_clue(self, x, y, grid):
        """Calculate clue value for a position"""
        total = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if grid[nx][ny] == 't':
                    total += 1
                elif grid[nx][ny] == 'l':
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

if __name__ == "__main__":
    generator = PuzzleGenerator(size=9, difficulty='medium')
    # puzzle, solution = generator.create_puzzle()
    puzzle = [['','_',0],['_',1,'_'],['_',-1,-1]]

    solution = PuzzleSolver.solve(0, 0, np.full((puzzle.size, puzzle.size)))