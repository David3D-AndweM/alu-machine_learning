#!/usr/bin/env python3
"""Module for numpy element-wise operations"""


def np_elementwise(mat1, mat2):
    """Perform element-wise operations on numpy arrays"""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
