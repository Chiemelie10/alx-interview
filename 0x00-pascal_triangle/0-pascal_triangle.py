#!/usr/bin/python3
"""This module defines a function that genrates the Pascal's Triangle."""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers representing the
    Paschal's triangle of n.
    It also returns an empty list if n <= 0.
    n is assumed to always be an integer.
    """

    if n <= 0:
        return []

    result = [[1]]

    for i in range(n - 1):
        temp = [0] + result[-1] + [0]
        next_row = []
        for j in range(len(result[-1]) + 1):
            next_row.append(temp[j] + temp[j + 1])
        result.append(next_row)
    return result
