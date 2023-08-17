def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise.

    Args:
        matrix (list[list]): The input matrix.

    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Store top-left element
            temp = matrix[i][j]
            # Move bottom-left element to top-left
            matrix[i][j] = matrix[n - 1 - j][i]
            # Move bottom-right element to bottom-left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            # Move top-right element to bottom-right
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            # Move top-left (stored) element to top-right
            matrix[j][n - 1 - i] = temp
