#!/usr/bin/env python3
"""Module for calculating adjugate matrix"""


def adjugate(matrix):
    """Calculates the adjugate matrix of a matrix"""
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

    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            submatrix = []
            for row_idx in range(n):
                if row_idx != i:
                    subrow = []
                    for col_idx in range(n):
                        if col_idx != j:
                            subrow.append(matrix[row_idx][col_idx])
                    submatrix.append(subrow)

            minor_val = determinant(submatrix)
            cofactor_val = ((-1) ** (i + j)) * minor_val
            cofactor_row.append(cofactor_val)

        cofactor_matrix.append(cofactor_row)

    adjugate_matrix = []
    for j in range(n):
        adj_row = []
        for i in range(n):
            adj_row.append(cofactor_matrix[i][j])
        adjugate_matrix.append(adj_row)

    return adjugate_matrix


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
