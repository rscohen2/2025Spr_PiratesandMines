# Treasure Hunt and Mines

# Puzzle Overview

In this puzzle, you are given a grid of possible sizes 4x4 to 9x9. In the grid, there are numbers and empty squares. Similar to mindsweeper, the numbers are clues to placement of landmines! Unlike mindsweeper, cells in the grid do not move, and there is also the potential to gain treasure! The objective of the puzzle is to figure out which empty cells are landmines, and which are treasure. 

To solve the puzzle, you use the given number clues to deterministically solve the positions of the mines and treasure squares. For each clue cell, for the basic or easy version of the puzzle, the clue is a sum of the landmines (-1) and treasures (+1) surronding that particular clue cell in all orthogonal directions (up, down, left, right). For instance, a clue of 0 could mean that cell is surronded by two treasures (+2) and two landmines (-2)  2-2= 0. 
For a version of the puzzle with increased difficulty, you must also consider diagonals, rather than just the orthogonal direction clues.

# How to play
Clone the repo and run the "app.py" script. Click one of the two links in the output to open the UI for the puzzle in your browser.


# Python Scripts in the Repo

## Puzzle Generation
This script creates a completed/fully solved puzzle with clues and landmines and treasures filled in, and subsequently removes the landmines and treasures in order to create a puzzle without an answer key. This solver also checks to make sure that there is only one valid solution for the generated puzzle by iterating recursively to see if there is any solution for the puzzle that hasn't already been recorded in its potential solution list.

## Toggle puzzle size and difficulty
Our scripts can generate varying puzzle sizes and difficulties.
### Difficulty
#### Easy
Clues are only the sum of orthogonal directions.
#### Difficult
Clues are the sum of both orthogonal and diagonal directions.

### Puzzle Size
The puzzle can be toggled to any size from 4x4 to 9x9.

## Solver Script (And Algorithm)
Our solver script takes an unsolved puzzle and uses a brute force technique to discover the solution. It fills all of the empty cells with treasure, checks to see if any rules/clues are no longer possible/valid with the configuration present after adding the last treasure it input, and then decides whether to change it to a landmine instead. It also uses backtracking to ensure that all clues remain valid.

## Data Structure
We chose to utilize an array to represent our puzzle due to it being convenient for representing and mapping the grid structure of our puzzle. Each cell has a coordinate x,y pair corresponding to its position in the grid, and allowing us to update the array of our puzzle.

# Puzzle Analysis

## Targeted Algorithm Analysis
When sorted by "Own Time" in the PyCharm Profiler, it looks like 
![img.png](profiling/img.png)

create_puzzle (0.001 s)

Dominant cost for this small 9×9 puzzle. Includes random fill, clue computation, and a full uniqueness check.

_solve recursion (82 calls)

The backtracking solver is naturally the hotspot—each empty cell branches two ways and validates adjacent clues.

Clue functions (_calculate_clues & _get_neighbor_sum)

Even though they’re lightweight here, they’ll scale as O(n²) for an n×n grid.

Optimization Suggestions
Early Pruning in Solver
Stop exploring a branch as soon as a clue check fails, rather than validating all neighbors.

Memoize Neighbor Sums
Cache results of _calculate_clue for cells whose neighborhood hasn’t changed.

Vectorize Clue Calculation
For initial clue grid, consider NumPy convolution with a kernel [[0,1,0],[1,0,1],[0,1,0]], mapping 't'→+1, 'l'→−1.

Limit Uniqueness Checks
If only >1 solution matters, modify count_solutions() to bail out as soon as solution_count > 1

## Big O Analysis

![img_1.png](profiling/img_1.png)

When you instantiate the PuzzleGenerator, you allocate two full n×n arrays (self.grid and self.clue_grid), so construction costs O(n²) time and O(n²) space. Filling the grid randomly and computing every clue via _calculate_clues() also takes exactly one pass over all n² cells; since each cell’s neighbor sum inspects only its four orthogonal neighbors, each is constant-time work, and the entire clue computation remains O(n²). The create_puzzle() method simply wraps these O(n²) steps and then calls generate_valid_solution(), which itself does one random-fill pass (O(n²)), one clue pass (O(n²)), and then hands off to the solver to verify uniqueness.

That hand‐off is critical: PuzzleSolver.count_solutions() is a pure backtracking routine over each of the k unknown cells. At each “?” cell it branches in two directions (“t” or “l”), so in the worst case it explores on the order of 2ᵏ partial grids. At each placement it does a constant-time validity check of up to four neighboring clues, and—if you choose to validate the completed grid at the leaves—another O(n²) pass. Altogether, the solver runs in O(2ᵏ · n²) time, with O(k) recursion‐stack space (plus whatever it takes to store any solutions you append).

Because your generator repeatedly invokes this exponential‐time solver until exactly one solution remains, the overall time complexity of puzzle creation is dominated by that backtracking check: on the order of 2ᵏ · n², which is exponential in the number of unknown cells. All of the other methods—initialization, clue computation, neighbor‐summing—are polynomial (O(n²) or O(1)) and become relatively insignificant once k grows.

--------------
## Indiviual Contributions to the Project:
### Becca
Developed the puzzle concept and structured a basic generator and solver for a sample puzzle, outlined backtracking algorithm that was implemented and debugged by Vedant. Implemented the diagonal toggle portion of the code into the generator, solver and the UI. Led project management/task delegation. Wrote the ReadMe and outline for presentation.
### Ke
Created an original UI for the project using Flask that allows dynamic visualization of puzzle solving, validating and puzzle toggle options. 
### Vedant
Improved Becca's basic solver to work on dynamic puzzle sizes, and created a working backtracker algorithm. Led and completed the Big-O and algorithm efficency analysis.


