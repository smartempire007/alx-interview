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

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    N = int(sys.argv[1])  # number of queens
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)
except ValueError:
    print('N must be a number')
    sys.exit(1)


def resolve_queens(row, queen, positions):
    """Resolve reachable range of queens"""

    positions.append(row)

    for i in queen[:]:
        if any([i == row, i[0] == row[0], i[1] == row[1],
                i[0] + i[1] == row[0] + row[1],
                i[0] - i[1] == row[0] - row[1]]):
            queen.pop(queen.index(i))

    if len(queen) == 0:
        if len(positions) == N:
            print(positions)
        return

    for j in [i for i in queen if i[1] > row[1] and i[0] != row[0]]:
        resolve_queens(j, queen[:], positions[:])


for i in range(N):
    resolve_queens([i, 0], [[x, y] for x in range(N)
                            for y in range(N)], [])
