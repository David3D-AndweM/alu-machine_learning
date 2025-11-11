#!/usr/bin/env python3
"""
Module for 2D matrix element-wise addition
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise
    
    Args:
        mat1: First 2D matrix (list of lists)
        mat2: Second 2D matrix (list of lists)
    
    Returns:
        A new matrix with element-wise sum, or None if shapes don't match
    """
    # Check if matrices have same number of rows
    if len(mat1) != len(mat2):
        return None
    
    # Check if matrices have same number of columns
    for i in range(len(mat1)):
        if len(mat1[i]) != len(mat2[i]):
            return None
    
    # Perform element-wise addition
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    
    return result