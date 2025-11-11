#!/usr/bin/env python3
"""
Module for matrix transpose
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix
    
    Args:
        matrix: A 2D matrix (list of lists)
    
    Returns:
        A new matrix that is the transpose of the input matrix
    """
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create new matrix with swapped dimensions
    transpose = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)
    
    return transpose
