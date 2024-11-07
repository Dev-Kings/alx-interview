#!/usr/bin/python3
"""
Module containing functions that solve the N-Queens Problem using backtracking
"""
import sys


def solve_nqueens(n):
    """
    Solves the N-Queens problem using backtracking and prints all
    the solutions.

    This function sets up a recursive backtracking algorithm to find
    all the possible ways to place N non-attacking queens on an N×N
    chessboard. For each solution, it prints the positions of the queens
    as a list of lists, where each inner list contains the row and column
    of a queen.

    Args:
        n (int): The size of the chessboard (N×N) and the number of queens
        to place.

    Returns:
        None: This function prints the solutions directly.
    """
    def is_valid(board, row, col):
        """
        Checks if it's valid to place a queen at the given position.

        A queen is placed at position (row, col). This function checks if the
        position is valid, i.e., no other queens are in the same column or
        diagonal.

        Args:
            board (list): A list representing the current state of the board,
            where the index represents the row, and the value represents the
            column of the queen.
            row (int): The current row where the queen is to be placed.
            col (int): The column where the queen is to be placed.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        """
        Recursively places queens on the chessboard using backtracking.

        This function tries placing a queen in each column of the current
        row and recursively proceeds to the next row. When a solution is
        found, it is printed.

        Args:
            board (list): A list representing the current state of the board,
            where the index represents the row, and the value represents the
            column of the queen.
            row (int): The current row where we are placing a queen.

        Returns:
            None: This function prints the solutions directly and modifies
            the board.
        """
        if row == n:
            # Print the current solution in the required format
            print([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1  # Reset for backtracking

    # Initialize the board with -1 (no queen placed)
    board = [-1] * n
    # Start the backtracking process from the first row
    backtrack(board, 0)


def main():
    """
    The main function that handles command-line arguments and calls the
    solve_nqueens function to solve the N queens problem.

    This function validates the input arguments to ensure the program is being
    executed with a valid integer (N) that is greater than or equal to 4. If
    the input is invalid, it prints the appropriate error message and exits
    with status 1.

    Returns:
        None: This function does not return any value; it either exits or
        calls solve_nqueens based on input validity.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem for the given N
    solve_nqueens(n)


if __name__ == "__main__":
    main()
