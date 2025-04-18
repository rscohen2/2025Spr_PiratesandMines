from generate_puzzle import generate_unsolved_puzzle
from generate_puzzle import get_clues
import numpy as np
import random

class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(6)] for _ in range(6)]
        self.grid_size = (6, 6)
        self.game_over = False

t = 1
e = 0
l = -1

example_board = [['','_',0],['_',1,'_'],['_',-1,-1]]

example_board_solved = [[t,t,0],[t,1,l],[l,-1,-1]]


# Function to convert cell values to numbers
def cell_value(val):
    if val == 't':
        return 1
    elif val == 'l':
        return -1
    try:
        return int(val)
    except ValueError:
        return 0


def check_clue(x,y, grid, clue_grid):
    grid = np.array(grid)
    rows, cols = grid.shape
    if grid[x, y] != 'l' and grid[x, y] != 't':
        cell_clue = 0
        empty_neighbors_count = 0
        directions = {
            'cell_right': (x + 1, y),
            'cell_left': (x - 1, y),
            'cell_above': (x, y + 1),
            'cell_below': (x, y - 1)}
        for dir_name, (nx, ny) in directions.items():
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbor_value = grid[nx, ny]
                if neighbor_value != ' ':
                    cell_clue += cell_value(neighbor_value)
                else:
                    empty_neighbors_count += 1

                if cell_clue == clue_grid[x, y]:
                    return True
                    # if cell_clue + 1*empty_neighbors_count or cell_clue -1*empty_neighbors_count == clue_grid[x, y]:
                    #     return True
                if cell_clue + generate_permutation(empty_neighbors_count) == clue_grid[x, y]:
                    return True
                return False



def generate_permutation(n):
    # Choose how many -1s and 1s you want (e.g., equal split)
    half = n // 2
    remainder = n % 2

    values = [-1] * half + [1] * half

    if remainder:  # If n is odd, add one more randomly
        values.append(random.choice([-1, 1]))

    random.shuffle(values)  # Shuffle to get a random permutation
    return values

# Example usage
permutation = generate_permutation(7)
print(permutation)


def brute_force(grid, puzzle):
    grid = np.array(grid)
    rows, cols = grid.shape

    for x in range(rows):
        for y in range(cols):
            if grid[x, y] == 'e':
                grid[x][y] = 't'
                if check_clue(x, y, grid, puzzle):
                    continue
                else:
                    grid[x][y] = 'l'
                    if check_clue(x, y, grid, puzzle):
                        continue
                    else:
                        break
    return grid

    #all permutations that might possibly work
    #predictable/simple sequence to try, so that any backtracking is as simple as possible also
    #if layout not valid at all reject the whole thing, if not possible to get that clue
    #if all empties and middle piece less than 4, then 2 must be treasure and 2 must be landmines etc
    #or use it to shortcut some of the brute force combinations
    #if all three full, might deduct last one
    #backtrack to look for any other soln
    #erase Ls until last T so becomes L and doesnt work, keep backtracking
    #backtrack all the way back to beginning, flip to last choice and breaks, cut off half the entire search spoace right away
    #not is it correct, but a contradiction/any clue that isn't possible with that configuration

    #example code for dominosa, didn't fill the entire thing before

    #could generate combos with multiple solns


    # for x in range(rows):
    #     for y in range(cols):
    #         if grid[x, y] == 'e':
    #             grid[x][y] = 't'
    #         # if grid[x, y] == 'e':
    #         #         grid[x, y] = 't'
    # for x in range(rows):
    #     for y in range(cols):
    #         if grid[x][y] == 't' or grid[x][y] == 'l':
    #             if check_clue(x, y, grid, puzzle):
    #                 # break
    #                 continue
    #                     # backtrack
    #             else:
    #                 grid[x,y] = 'l'
    #                 if check_clue(x, y, grid, puzzle):
    #                     continue
    #                 else:
    #                     grid[x, y] = 'e'
    # return grid



def validate_entire_grid(grid, puzzle):
    rows, cols = grid.shape
    for x in range(rows):
        for y in range(cols):
            if not check_clue(x, y, puzzle, grid):
                return False
    return True







if __name__ == "__main__":
    game = Game()
    puzzle = generate_unsolved_puzzle(6,6)
    solution = puzzle.copy()
    potential_solution = brute_force(puzzle, solution)
    print(potential_solution)



