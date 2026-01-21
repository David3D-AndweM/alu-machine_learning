#!/usr/bin/env python3
"""
Module for calculating the adjugate matrix of a given matrix.
"""


def adjugate(matrix):
    """
    Calculate the adjugate matrix of a given matrix.
    
    The adjugate matrix (also called adjoint matrix) is the transpose of the
    cofactor matrix. It is used in calculating the inverse of a matrix.
    
    Args:
        matrix: A list of lists whose adjugate matrix should be calculated
        
    Returns:
        The adjugate matrix of matrix
        
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
    
    # Calculate cofactor matrix first
    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
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
            
            # Calculate minor (determinant of submatrix)
            minor_val = determinant(submatrix)
            
            # Apply cofactor sign: (-1)^(i+j)
            cofactor_val = ((-1) ** (i + j)) * minor_val
            cofactor_row.append(cofactor_val)
        
        cofactor_matrix.append(cofactor_row)
    
    # Transpose the cofactor matrix to get adjugate
    adjugate_matrix = []
    for j in range(n):
        adj_row = []
        for i in range(n):
            adj_row.append(cofactor_matrix[i][j])
        adjugate_matrix.append(adj_row)
    
    return adjugate_matrix


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