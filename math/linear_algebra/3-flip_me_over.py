#!/usr/bin/env python3
"""Module for matrix transpose"""


def matrix_transpose(matrix):
    """Transpose a 2D matrix"""
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]
