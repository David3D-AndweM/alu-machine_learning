#!/usr/bin/env python3


def minor(matrix):
    """Calculates the minor matrix of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    
    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")
    
    if n == 1:
        return [[1]]
    
    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            submatrix = []
            for row_idx in range(n):
                if row_idx != i:
                    subrow = []
                    for col_idx in range(n):
                        if col_idx != j:
                            subrow.append(matrix[row_idx][col_idx])
                    submatrix.append(subrow)
            
            det = determinant(submatrix)
            minor_row.append(det)
        
        minor_matrix.append(minor_row)
    
    return minor_matrix


def determinant(matrix):
    """Calculates the determinant of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    
    if len(matrix) == 0:
        return 1
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")
    
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        submatrix = []
        for i in range(1, n):
            subrow = []
            for k in range(n):
                if k != j:
                    subrow.append(matrix[i][k])
            submatrix.append(subrow)
        
        cofactor = ((-1) ** j) * matrix[0][j] * determinant(submatrix)
        det += cofactor
    
    return det