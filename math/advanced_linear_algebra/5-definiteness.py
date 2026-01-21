#!/usr/bin/env python3
"""
Module for determining the definiteness of a matrix.
"""


def definiteness(matrix):
    """
    Calculate the definiteness of a matrix.
    
    A matrix can be classified as:
    - Positive definite: all eigenvalues > 0
    - Positive semi-definite: all eigenvalues >= 0
    - Negative definite: all eigenvalues < 0
    - Negative semi-definite: all eigenvalues <= 0
    - Indefinite: has both positive and negative eigenvalues
    
    This implementation uses Sylvester's criterion (leading principal minors)
    for symmetric matrices.
    
    Args:
        matrix: A list of lists representing a square matrix
        
    Returns:
        A string indicating the definiteness:
        'Positive definite', 'Positive semi-definite',
        'Negative definite', 'Negative semi-definite',
        'Indefinite', or None if matrix is not square or symmetric
        
    Raises:
        TypeError: If matrix is not a list of lists
    """
    # Input validation
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    
    if len(matrix) == 0:
        return None
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is square
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return None
    
    # Check if matrix is symmetric
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return None
    
    # Use Sylvester's criterion: check leading principal minors
    leading_minors = []
    
    for k in range(1, n + 1):
        # Extract k x k leading principal submatrix
        submatrix = []
        for i in range(k):
            subrow = []
            for j in range(k):
                subrow.append(matrix[i][j])
            submatrix.append(subrow)
        
        # Calculate determinant of this submatrix
        minor = determinant(submatrix)
        leading_minors.append(minor)
    
    # Apply Sylvester's criterion
    # Positive definite: all leading minors > 0
    if all(minor > 0 for minor in leading_minors):
        return "Positive definite"
    
    # Negative definite: alternating signs starting with negative
    # (-1)^k * M_k > 0 for all k
    negative_definite = True
    for k, minor in enumerate(leading_minors, 1):
        if ((-1) ** k) * minor <= 0:
            negative_definite = False
            break
    
    if negative_definite:
        return "Negative definite"
    
    # For semi-definite cases, we need to check if the matrix is singular
    # and examine the signs more carefully
    det_full = leading_minors[-1]  # determinant of full matrix
    
    # If determinant is 0, matrix is singular (semi-definite possible)
    if det_full == 0:
        # Check if all leading minors are non-negative
        if all(minor >= 0 for minor in leading_minors):
            return "Positive semi-definite"
        
        # Check if alternating pattern holds with non-positive constraint
        negative_semi = True
        for k, minor in enumerate(leading_minors, 1):
            if ((-1) ** k) * minor < 0:
                negative_semi = False
                break
        
        if negative_semi:
            return "Negative semi-definite"
    
    # If none of the above, it's indefinite
    return "Indefinite"


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