#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a
floating-point number.

The `floor` function takes a float and returns the greatest 
integer less than or equal to the input.
"""


import math
def floor(n: float) -> int:
    result = math.floor(n)
    return result
