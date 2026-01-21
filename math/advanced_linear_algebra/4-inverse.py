#!/usr/bin/env python3
"""
Module for calculating the inverse of a given matrix.
"""


def inverse(matrix):
    """
    Calculate the inverse of a given matrix.
    
    The inverse of a matrix A is a matrix A^(-1) such that A * A^(-1) = I,
    where I is the identity matrix. The inverse is calculated as:
    A^(-1) = (1/det(A)) * adj(A), where det(A) is the determinant and
    adj(A) is the adjugate matrix.
    
    Args:
        matrix: A list of lists whose inverse should be calculated
        
    Returns:
        The inverse matrix of matrix, or None if matrix is not invertible
        
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
    
    # Calculate determinant
    det = determinant(matrix)
    
    # If determinant is 0, matrix is not invertible
    if det == 0:
        return None
    
    # Special case: 1x1 matrix
    if n == 1:
        return [[1 / matrix[0][0]]]
    
    # Calculate adjugate matrix
    adj_matrix = adjugate(matrix)
    
    # Calculate inverse: (1/det) * adjugate
    inverse_matrix = []
    for i in range(n):
        inverse_row = []
        for j in range(n):
            inverse_row.append(adj_matrix[i][j] / det)
        inverse_matrix.append(inverse_row)
    
    return inverse_matrix


def adjugate(matrix):
    """
    Calculate the adjugate matrix of a given matrix.
    
    Args:
        matrix: A list of lists whose adjugate matrix should be calculated
        
    Returns:
        The adjugate matrix of matrix
    """
    n = len(matrix)
    
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
    """
    if len(matrix) == 0:
        return 1
    
    n = len(matrix)
    
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