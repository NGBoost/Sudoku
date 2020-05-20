# This script contains helper functions to solve the Sudoku puzzle.
import numpy as np

def is_valid(grid, num, pos):
    """
    Determines whether it will be legal to assign num to the given row,col.

    Args:
        grid: The Sudoku board. Format: 2D nested lists of integers.
        num: The number we want to test if it is valid in the given position.
        pos: The position.

    Returns:
        A boolean which indicates whether it will be legal to assign num to given row,column location.
    """
    # Check the row.
    for i in range(len(grid)):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the column.
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the subgrid.
    subgrid_x = (pos[0] // 3) * 3
    subgrid_y = (pos[1] // 3) * 3
    for i in range(subgrid_x, subgrid_x + 3):
        for j in range(subgrid_y, subgrid_y + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def empty_square(grid):
    """ Finds an empty square in the Sudoku board and return the position.

    Args:
        grid: The Sudoku board. Format: 2D nested lists of integers.

    Returns:
        Either a tuple representing the position of the empty square. (row,column).
        Or None if there is not an empty square.
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return (i, j)

    return None

def solve(grid):
    """
    Solve the Sudoku puzzle using recursion and backtracking.
    Takes a partially unassigned filled-in grid and attempts to find a solution.

    Args:
        grid: The Sudoku grid. Format: 2D nested lists of integers.

    Returns:
        True if there is a feasible solution, False if not.
        N.B. If there is a feasible solution, after the execution of the function we can print the Sudoku solution.
    """
    emp_sqr = empty_square(grid)

    if emp_sqr is None:
        print("-----------------------")
        print('Solved!')
        print('Solution:')
        print(np.matrix(grid))
        return True
    else:
        row = emp_sqr[0]
        col = emp_sqr[1]

    for i in range(1,10):
        if is_valid(grid, i, (row, col)):
            grid[row][col] = i

            # recursion
            if solve(grid):
                return True

            # trigger backtracking
            grid[row][col] = 0

    return False
