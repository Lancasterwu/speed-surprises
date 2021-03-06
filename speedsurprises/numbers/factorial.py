"""Compute the numerical factorial function"""

# Source and/or inspiration for the function(s):
# https://is.gd/GIibZB

# Worst-case time complexity: O(n) -- Linear


def compute_factorial(value):
    """Assumes value is a natural number
    Returns value!"""
    answer = 1
    while value > 1:
        answer *= value
        value = value - 1
    return answer
