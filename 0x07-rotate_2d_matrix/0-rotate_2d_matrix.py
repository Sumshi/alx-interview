#!/usr/bin/python3
"""This module defines a function `rotate_2d_matrix`"""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix 90 degrees clockwise"""
    n = len(matrix)

    # swap the position of each matrix element
    for r in range(n):
        for c in range(r, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # reverse the rows
    for array in matrix:
        array.reverse()
