#!/usr/bin/python3
"""
Python module that calculates the fewest number of operations needed
to result in a given number of desired characters """


def minOperations(n):
    """
    Calculates fewest number of operations needed to result in exactly
    n H characters in the file.
    Args:
        n (int): The desired number of H characters in the file.
    Returns:
        min number of operations needed or 0 if n is impossible to achieve"""

    min_ops = 0  # Initialize the total operations needed

    if n <= 1:
        return 0

    # Iterate through numbers from 2 to n
    for i in range(2, n + 1):
        # While n is divisible by i,
        # keep dividing n by i and increment operations by i
        while n % i == 0:
            n = n / i  # Divide n by i

            # Increment operations by i, as i rep number of times 'i' is pasted
            min_ops += i
    return min_ops
