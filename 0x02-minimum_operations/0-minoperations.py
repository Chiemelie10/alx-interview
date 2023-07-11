#!/usr/bin/python3
"""This module defines the function 'minOperations'."""

from typing import Set, List


def minOperations(n: int) -> int:
    """
    This function calculates the minimum number of operatons needed to
    'copy' and 'paste' letter 'H' n number of times in a file.
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations
