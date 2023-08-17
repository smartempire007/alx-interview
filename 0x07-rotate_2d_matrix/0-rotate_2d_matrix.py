#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise.
Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will
not be empty.
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list[list]): The input matrix to be rotated.

    Returns:
        None: The matrix is modified in-place.
    """

    n = len(matrix)  # Get the size of the matrix

    copy = matrix[:]  # Create a copy of the original matrix

    # Iterate through each element in the matrix
    for y in range(n):
        dx = []

        # Iterate through each column in reverse order
        for x in range(n-1, -1, -1):
            # Append elements from each column to a new row list (dx)
            dx.append(matrix[x][y])
        # Add the new row list (dx) to the original matrix
        matrix.append(dx)

    # Remove the original rows from the matrix
    for dx in copy:
        matrix.pop(matrix.index(dx))
