#!/usr/bin/env python3
import numpy as np


def definiteness(matrix):
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    
    if matrix.size == 0:
        return None
    
    if len(matrix.shape) != 2:
        return None
    
    n, m = matrix.shape
    if n != m:
        return None
    
    if not np.allclose(matrix, matrix.T):
        return None
    
    leading_minors = []
    
    for k in range(1, n + 1):
        submatrix = matrix[:k, :k]
        minor = np.linalg.det(submatrix)
        leading_minors.append(minor)
    
    if all(minor > 0 for minor in leading_minors):
        return "Positive definite"
    
    negative_definite = True
    for k, minor in enumerate(leading_minors, 1):
        if ((-1) ** k) * minor <= 0:
            negative_definite = False
            break
    
    if negative_definite:
        return "Negative definite"
    
    det_full = leading_minors[-1]
    
    if abs(det_full) < 1e-10:
        if all(minor >= -1e-10 for minor in leading_minors):
            return "Positive semi-definite"
        
        negative_semi = True
        for k, minor in enumerate(leading_minors, 1):
            if ((-1) ** k) * minor < -1e-10:
                negative_semi = False
                break
        
        if negative_semi:
            return "Negative semi-definite"
    
    return "Indefinite"