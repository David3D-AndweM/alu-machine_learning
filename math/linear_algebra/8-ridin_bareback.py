#!/usr/bin/env python3
"""
Module for matrix multiplication
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication
    
    Args:
        mat1: First 2D matrix (list of lists)
        mat2: Second 2D matrix (list of lists)
    
    Returns:
        A new matrix that is the product of mat1 and mat2, or None if cannot multiply
    """
    # Check if matrices can be multiplied
    # mat1 columns must equal mat2 rows
    if len(mat1[0]) != len(mat2):
        return None
    
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    cols2 = len(mat2[0])
    
    # Initialize result matrix with zeros
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            row.append(0)
        result.append(row)
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result
