from generate_puzzle import generate_unsolved_puzzle
from generate_puzzle import get_clues
import numpy as np

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
                    if cell_clue == clue_grid[x,y]:
                        return True
                    else:
                        return False

def brute_force(grid, puzzle):
    grid = np.array(grid)
    rows, cols = grid.shape

    for x in range(rows):
        for y in range(cols):
            if grid[x, y] == 'e':
                    grid[x, y] = 't'
                    if check_clue(x, y, grid, puzzle):
                        break
                    # backtrack
                    else:
                        grid[x,y] = 'l'
                        if check_clue(x, y, grid, puzzle):
                            break
                        else:
                            grid[x, y] = 'e'
    return grid



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



