#!/usr/bin/env python3

if __name__ == '__main__':
    definiteness = __import__('5-definiteness').definiteness

    mat1 = [[5, 1], [1, 1]]
    mat2 = [[2, 4], [4, 8]]
    mat3 = [[-1, 1], [1, -1]]
    mat4 = [[-2, 4], [4, -9]]
    mat5 = [[1, 2], [1, 1]]
    mat6 = []
    mat7 = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]

    print(definiteness(mat1))
    print(definiteness(mat2))
    print(definiteness(mat3))
    print(definiteness(mat4))
    print(definiteness(mat5))
    print(definiteness(mat6))
    print(definiteness(mat7))