# This script contains helper functions to solve the Sudoku puzzle.

import numpy as np

def is_valid(grid, num, pos):
    """Determines whether it will be legal to assign num to the given row,col.

    Args:
        grid: 2D nested lists of integers. The Sudoku board.
        num: The number we want to test if it is valid in the given position.
        pos: The position.

    Returns:
        A boolean which indicates whether it will be legal to assign num to given row,column location.
    """
    # Check the row.
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the column.
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the box.
    box_x = (pos[0] // 3) * 3
    box_y = (pos[1] // 3) * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def empty_square(grid):
    """Finds an empty square in the Sudoku board and return the position.

    Args:
        grid: 2D nested lists of integers. The Sudoku board.

    Returns:
        Either a tuple representing the position of the empty square (row,column),
        or None if there is not an empty square.
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)

    return None

def solve(grid):
    """A Sudoku solver.
    
    A solver that finds one of the possible solutions of a Sudoku board,
    by recursively backtracking through entry values.

    Args:
        grid: 2D nested lists of integers. This is an unsolved Sudoku board, with 0's as unknown values.

    Returns:
        True if there is a feasible solution and prints the Sudoku solution, False if the solution is not.
    """
    emp_sqr = empty_square(grid)

    if emp_sqr is None:
        print("-----------------------")
        print('Solved!')
        print('Solution:')
        print_board(grid)
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

def print_board(grid):
    """Print the Sudoku board.

    Args:
        grid: 2D nested lists of integers. The Sudoku board.

    Returns:
        A user friendly visual representation of the Sudoku board.
    """
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - -")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")
