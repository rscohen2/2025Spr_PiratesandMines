"""
This page calls from the solver and generate_puzzle scripts to run a flask app using these two scripts to generate and solve our puzzle.
In this header, we also wish to disclose that ChatGPT was used as a debugging tool in a few cases. For instance, ChatGPT had recommended the "<U4" fix that fixed an error where '-' (a negative sign) was being displayed rather than the full clue for negative clues.

For the multiple solution bug, we realized the solver was not properly finding all the solutions to a particular puzzle, and while a correct solution was printed in the output itself, the solution stored in the list was all 'e' cells.
This was due to a mix of 'e' and '?' being used in different stages of the puzzle where the other should have been used instead.
In addition, there was a confusing use of 0 being used for both non-clue cells due to the int structure of the np array. Thus, I changed the structure to str data type in order to mark non-clue cells as 'e' instead of 0. When they were marked as 0, it was difficult to tell which were actually non-clue cells, and which were clue cells with a value of 0.
Finally, the backtracking algorithm was not checking first for a valid solution, which caused the issue of the solution stored in the solution list to become all 'e's since the if statement condition was always met.

For removing the grid.copy() so that our big O was accurate, we saved the original grid to a variable instead, so that we could revert any changes made at the end of the function without creating an entirely new object to be stored in memory.

"""

from flask import Flask, request, jsonify, render_template, send_from_directory
import numpy as np
import os
import json

from generate_puzzle import PuzzleGenerator
from solver import PuzzleSolver

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    """Serve the main index page"""
    return send_from_directory('static', 'index.html')

@app.route('/game')
def game():
    """Serve the game page"""
    return send_from_directory('static', 'game.html')

@app.route('/api/generate_puzzle', methods=['POST'])
def generate_puzzle():
    """API endpoint to generate a puzzle based on size and difficulty"""
    # Get parameters from request
    data = request.get_json()
    size = int(data.get('size', 6))
    # difficulty = data.get('difficulty', 'medium')
    diagonal = data.get('diagonal', False)
    
    # Validate parameters
    if size not in [4, 6, 8, 9]:
        return jsonify({'error': 'Invalid size. Must be 4, 6, 8, or 9.'}), 400
    
    # if difficulty not in ['easy', 'medium', 'hard']:
    #     return jsonify({'error': 'Invalid difficulty. Must be easy, medium, or hard.'}), 400
    
    try:
        generator = PuzzleGenerator(size=size, diagonal=diagonal)
        puzzle, solution = generator.create_puzzle()
        
        # Convert numpy arrays to lists if needed
        if isinstance(puzzle, np.ndarray):
            puzzle = puzzle.tolist()
        if isinstance(solution, np.ndarray):
            solution = solution.tolist()
        
        # Print solution to console for debugging
        print("\n===== PUZZLE SOLUTION =====")
        for row in solution:
            print(row)
        print("===========================\n")
        
        # Return the puzzle and solution
        return jsonify({
            'puzzle': puzzle,
            'solution': solution,
            'diagonal': diagonal
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/verify_solution', methods=['POST'])
def verify_solution():
    """API endpoint to verify a player's solution"""
    try:
        data = request.get_json()
        player_grid = data.get('playerGrid', [])
        solution = data.get('solution', [])
        
        print("Received verification request:")
        print(f"Player grid shape: {len(player_grid)}x{len(player_grid[0]) if player_grid else 0}")
        print(f"Solution shape: {len(solution)}x{len(solution[0]) if solution else 0}")
        
        # Convert to numpy arrays for easier processing
        player_grid_np = np.array(player_grid)
        solution_np = np.array(solution)
        
        # Check if player solution matches the correct solution
        is_valid = True
        size = len(solution)
        
        for i in range(size):
            for j in range(size):
                # Skip clue cells in the puzzle
                if solution_np[i][j] == 'e':
                    continue
                
                # Check if player's choice matches the solution
                if solution_np[i][j] == 't' and player_grid_np[i][j] != 'treasure':
                    print(f"Mismatch at ({i},{j}): Expected treasure, got {player_grid_np[i][j]}")
                    is_valid = False
                    break
                if solution_np[i][j] == 'l' and player_grid_np[i][j] != 'mine':
                    print(f"Mismatch at ({i},{j}): Expected mine, got {player_grid_np[i][j]}")
                    is_valid = False
                    break
            
            if not is_valid:
                break
        
        print(f"Verification result: {'Valid' if is_valid else 'Invalid'}")
        
        return jsonify({
            'valid': is_valid
        })
    except Exception as e:
        import traceback
        print(f"Error in verify_solution: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

def check_valid_solution(player_grid, puzzle_grid, diagonal = False):
    """Check if player's solution satisfies all clues"""
    size = len(puzzle_grid)
    
    for i in range(size):
        for j in range(size):
            # Skip non-clue cells
            if puzzle_grid[i][j] == '?' or puzzle_grid[i][j] == 'e':
                continue
                
            # Get expected clue value
            expected_value = int(puzzle_grid[i][j]) if isinstance(puzzle_grid[i][j], str) else puzzle_grid[i][j]
            
            # Calculate actual sum from player's grid
            actual_value = 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

            # Add diagonals if enabled
            if diagonal:
                directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < size and 0 <= ny < size:
                    if player_grid[nx][ny] == 't':
                        actual_value += 1
                    elif player_grid[nx][ny] == 'l':
                        actual_value -= 1
            
            # If any clue is not satisfied, solution is invalid
            if actual_value != expected_value:
                return False
    
    return True

def calculate_score(player_grid):
    """Calculate score based on treasures and landmines"""
    score = 0
    for row in player_grid:
        for cell in row:
            if cell == 't':
                score += 1
            elif cell == 'l':
                score -= 1
    return score

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5001)