import random
import numpy as np

# Function to generate a solved puzzle with treasures and landmines
def generate_solved_puzzle(height, width):
    """
    Generates a random solved puzzle with treasures and landmines.
    """
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    nonempty_probability = 0.50  # Adjust to control puzzle difficulty

    for i in range(height):
        for j in range(width):
            if random.random() < nonempty_probability:
                grid[i][j] = random.choice(['t', 'l'])  # 't' for treasure, 'l' for landmine

    return grid

# Function to calculate clues for empty cells
def get_clues(grid):
    grid = np.array(grid)
    rows, cols = grid.shape

    def cell_value(val):
        if val == 't':
            return 1
        elif val == 'l':
            return -1
        return 0

    # Calculate clues for empty cells
    clues_grid = np.array(grid, dtype=object)  # Initialize clue grid with the same shape
    for x in range(rows):
        for y in range(cols):
            if grid[x, y] != 'l' and grid[x, y] != 't':  # Only for empty cells
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
                clues_grid[x, y] = cell_clue  # Store numeric clue in clue grid
    return clues_grid

# Function to display the puzzle grid with clues
def display_grid(grid):
    print("\nCurrent Grid:")
    for row in grid:
        print(' '.join(str(cell) for cell in row))

# Function to check if the grid is complete (game over)
def is_game_over(grid):
    for row in grid:
        if ' ' in row:  # If any cell is still empty
            return False
    return True

# Function to step-by-step solve the puzzle
def solve_puzzle(grid, clues_grid):
    """
    Step-by-step solving of the puzzle.
    """
    rows, cols = len(grid), len(grid[0])

    # Continue solving until the grid is complete
    while not is_game_over(grid):
        step_completed = False  # Flag to track if a step was completed in this iteration

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == ' ' and isinstance(clues_grid[x][y], int):  # Check for empty cells and valid clue
                    # If the clue is non-empty, place the correct value (treasure or landmine)
                    if clues_grid[x][y] > 0:
                        grid[x][y] = 't'  # Treasure (positive clue)
                    elif clues_grid[x][y] < 0:
                        grid[x][y] = 'l'  # Landmine (negative clue)

                    step_completed = True  # Step completed, update the grid
                    display_grid(grid)  # Display updated grid
                    break  # Exit the inner loop and proceed with the next step

            if step_completed:
                break  # Exit the outer loop and restart the process with updated grid

        if not step_completed:
            print("No progress made in this iteration. Something went wrong!")
            break

        print("------------- Step Complete -------------")

    print("\nPuzzle Solved! Final Grid:")
    display_grid(grid)

# Main function to run the game
def play_game(n):
    # Step 1: Generate a solved puzzle
    solved_puzzle = generate_solved_puzzle(n, n)

    # Step 2: Calculate clues
    clues_grid = get_clues(solved_puzzle)

    # Step 3: Initialize the empty grid for the user to interact with
    user_grid = [[' ' for _ in range(n)] for _ in range(n)]

    # Step 4: Display the initial grid with clues
    print("Puzzle Generated! Here are the clues:")
    display_grid(clues_grid)

    # Step 5: Step-by-step solution process
    print("\nNow, the puzzle will be solved step-by-step:")
    solve_puzzle(user_grid, clues_grid)

if __name__ == "__main__":
    grid_size = int(input("Enter the grid size (n x n): "))
    play_game(grid_size)
