#!/usr/bin/env python3

if __name__ == '__main__':
    adjugate = __import__('3-adjugate').adjugate

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print(adjugate(mat1))
    print(adjugate(mat2))
    print(adjugate(mat3))
    print(adjugate(mat4))
    try:
        adjugate(mat5)
    except Exception as e:
        print(e)
    print(adjugate(mat6))
