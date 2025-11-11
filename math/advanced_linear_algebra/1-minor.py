#!/usr/bin/env python3
"""
Module for calculating the minor matrix of a given matrix.
"""


def minor(matrix):
    """
    Calculate the minor matrix of a given matrix.
    
    The minor matrix is a matrix where each element (i,j) is the determinant
    of the submatrix obtained by removing row i and column j from the original matrix.
    
    Args:
        matrix: A list of lists whose minor matrix should be calculated
        
    Returns:
        The minor matrix of matrix
        
    Raises:
        TypeError: If matrix is not a list of lists
        ValueError: If matrix is not square or is empty
    """
    # Input validation
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    
    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is square
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")
    
    # Special case: 1x1 matrix
    if n == 1:
        return [[1]]
    
    # Calculate minor matrix
    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            # Create submatrix by removing row i and column j
            submatrix = []
            for row_idx in range(n):
                if row_idx != i:
                    subrow = []
                    for col_idx in range(n):
                        if col_idx != j:
                            subrow.append(matrix[row_idx][col_idx])
                    submatrix.append(subrow)
            
            # Calculate determinant of submatrix
            det = determinant(submatrix)
            minor_row.append(det)
        
        minor_matrix.append(minor_row)
    
    return minor_matrix


def determinant(matrix):
    """
    Calculate the determinant of a matrix using cofactor expansion.
    
    Args:
        matrix: A list of lists whose determinant should be calculated
        
    Returns:
        The determinant of matrix
        
    Raises:
        TypeError: If matrix is not a list of lists
        ValueError: If matrix is not square
    """
    # Input validation
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    
    if len(matrix) == 0:
        return 1
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is square
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")
    
    # Base cases
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case: cofactor expansion along first row
    det = 0
    for j in range(n):
        # Create submatrix by removing first row and column j
        submatrix = []
        for i in range(1, n):
            subrow = []
            for k in range(n):
                if k != j:
                    subrow.append(matrix[i][k])
            submatrix.append(subrow)
        
        # Calculate cofactor and add to determinant
        cofactor = ((-1) ** j) * matrix[0][j] * determinant(submatrix)
        det += cofactor
    
    return det