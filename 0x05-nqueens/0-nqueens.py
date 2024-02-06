#!/usr/bin/python3
"""This script solves the N-Queens problem"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

columns = set()
pos_diagonal = set()
neg_diagonal = set()
board = []

# create the board positions
for _ in range(N):
    row = [0] * 2
    board.append(row)


def is_safe(r, c):
    """Check if a queen can be placed at position (r, c)"""
    if c in columns or (r + c) in pos_diagonal or (r - c) in neg_diagonal:
        return False
    return True


def solve_n_queens(r):
    """recursively places N queens on an N x N chessboard"""
    if r == N:
        print(board)
        return

    for c in range(N):
        if is_safe(r, c):
            columns.add(c)
            pos_diagonal.add(r + c)
            neg_diagonal.add(r - c)
            board[r] = [r, c]
            solve_n_queens(r + 1)
            # Backtrack
            columns.remove(c)
            pos_diagonal.remove(r + c)
            neg_diagonal.remove(r - c)
            board[r] = [0, 0]


solve_n_queens(0)
