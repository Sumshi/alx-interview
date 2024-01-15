#!/usr/bin/python3
"""
If the number of H is divisible by n, copy and paste
else paste only
"""


def minOperations(n):
    """
    Returns the number of operations
    required to reach a certain n
    """
    Len_H = 1  # original length if H
    Len_copied_H = 0  # no copies are made at first
    total_operations = 0  # no operation has been made so far

    # break the loop when len_h == n
    while Len_H < n:
        if n % Len_H == 0:
            # perform copy and paste(2 operation)
            total_operations += 2
            Len_copied_H = Len_H
            Len_H *= 2
        else:
            # perform only 1 operation that is paste only
            total_operations += 1
            Len_H += Len_copied_H
    return total_operations
