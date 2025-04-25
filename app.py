from flask import Flask, request, jsonify, render_template, send_from_directory
import numpy as np
import os
import json

# Import your puzzle generator code
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
    difficulty = data.get('difficulty', 'medium')
    
    # Validate parameters
    if size not in [4, 6, 8, 9]:
        return jsonify({'error': 'Invalid size. Must be 4, 6, 8, or 9.'}), 400
    
    if difficulty not in ['easy', 'medium', 'hard']:
        return jsonify({'error': 'Invalid difficulty. Must be easy, medium, or hard.'}), 400
    
    try:
        # Generate puzzle using your existing code
        generator = PuzzleGenerator(size=size, difficulty=difficulty)
        puzzle, solution = generator.create_puzzle()
        
        # Convert numpy arrays to lists if needed
        if isinstance(puzzle, np.ndarray):
            puzzle = puzzle.tolist()
        if isinstance(solution, np.ndarray):
            solution = solution.tolist()
        
        # Return the puzzle and solution
        return jsonify({
            'puzzle': puzzle,
            'solution': solution
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/verify_solution', methods=['POST'])
def verify_solution():
    """API endpoint to verify a player's solution"""
    data = request.get_json()
    player_grid = data.get('playerGrid', [])
    puzzle_grid = data.get('puzzleGrid', [])
    
    try:
        # Convert to numpy arrays for easier processing
        player_grid_np = np.array(player_grid)
        puzzle_grid_np = np.array(puzzle_grid)
        
        # Check if player's solution satisfies all clues
        is_valid = check_valid_solution(player_grid_np, puzzle_grid_np)
        
        # Calculate score
        score = calculate_score(player_grid_np)
        
        return jsonify({
            'valid': is_valid,
            'score': score
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def check_valid_solution(player_grid, puzzle_grid):
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
    # Create a static folder for HTML files if it doesn't exist
    os.makedirs('static', exist_ok=True)
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5001)