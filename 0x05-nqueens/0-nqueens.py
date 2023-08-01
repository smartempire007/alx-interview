#!/usr/bin/python3
'''The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
if the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
if N is not an integer, print N must be a number, followed by a new line,
and exit with the status 1
if N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1
The program should print every possible solution to the problem
  One solution per line
  Format: see example
  You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
'''

import sys


class NQueen:
    """Class for solving N Queen Problem"""

    def __init__(self, n):
        """Global Variables"""
        self.n = n
        self.x = [0] * (n + 1)

    def place(self, k, i):
        """Checks if k Queen can be placed in i column (True)
        or if there are attacking queens in row or diagonal (False)
        """

        # j checks from 1 to k - 1 (Up to the previous queen)
        for j in range(1, k):
            # There is already a queen in the column
            # or a queen in the same diagonal
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def nQueen(self, k):
        """Tries to place every queen on the board
        Args:
        k: starting queen from which to evaluate (should be 1)
        """
        # i goes from column 1 to column n (1st column is 1st index)
        for i in range(1, self.n + 1):
            if self.place(k, i):
                # Queen can be placed in i column
                self.x[k] = i
                if k == self.n:
                    # Placed all N Queens (A solution was found)
                    yield [(i - 1, self.x[i] - 1) for i in range(1, self.n + 1)]
                else:
                    # Need to place more Queens
                    yield from self.nQueen(k + 1)


# Main

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
res = queen.nQueen(1)

for i in res:
    print(i)
