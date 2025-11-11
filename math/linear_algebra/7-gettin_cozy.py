#!/usr/bin/env python3
"""
Module for 2D matrix concatenation
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specific axis
    
    Args:
        mat1: First 2D matrix (list of lists)
        mat2: Second 2D matrix (list of lists)
        axis: Axis along which to concatenate (0 for rows, 1 for columns)
    
    Returns:
        A new matrix with concatenated data, or None if cannot concatenate
    """
    if axis == 0:
        # Concatenate along rows (stack vertically)
        # Check if matrices have same number of columns
        if len(mat1[0]) != len(mat2[0]):
            return None
        
        result = []
        for row in mat1:
            result.append(row[:])  # Copy row
        for row in mat2:
            result.append(row[:])  # Copy row
        return result
    
    elif axis == 1:
        # Concatenate along columns (stack horizontally)
        # Check if matrices have same number of rows
        if len(mat1) != len(mat2):
            return None
        
        result = []
        for i in range(len(mat1)):
            new_row = mat1[i][:] + mat2[i][:]  # Concatenate rows
            result.append(new_row)
        return result
    
    return None
