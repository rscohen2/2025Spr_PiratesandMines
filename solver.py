

class Game():
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



