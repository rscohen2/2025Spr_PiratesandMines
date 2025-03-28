
import random

class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(9)] for _ in range(9)]
        self.grid_size = (9, 9)
        self.game_over = False

t = 1
e = 0
l = -1

example_board = [['_','_',0],['_',1,'_'],['_',-1,-1]]

example_board_solved = [[t,t,0],[t,1,l],[l,-1,-1]]


def is_valid_board_complete(self):
    """
    Checks that a completely filled board.
    """
    for (i, j) in self.board:
        if self.grid[i][j] == ' ':
            return False  # board is not complete
    return True


def generate_puzzle(height, width):
    """
    Generates a random Haunted Mirror Maze puzzle of given height and width.
    The puzzle is created by randomly placing mirrors and then randomly distributing
    monsters over the remaining cells (to form a complete solution). Clues are computed
    from that solution. The solver is then used to verify that the puzzle (with monsters
    removed) has a unique solution. When a unique puzzle is generated, the puzzle
    (mirrors, clues, and monster counts) is printed to the console and the solution is
    written to a file named "solution.txt".
    """
    attempt = 0
    while True:
        attempt += 1
        # Create an empty grid (all cells start as empty monster cells).
        grid = [[' ' for _ in range(width)] for _ in range(height)]

        # Randomly place mirrors with a fixed probability (e.g., 25% chance).
        nonempty_probability = 0.25

        for i in range(height):
            for j in range(width):
                if random.random() < nonempty_probability:
                    grid[i][j] = random.choice(['l', 't'])
                return grid





