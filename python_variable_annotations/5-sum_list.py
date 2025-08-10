#!/usr/bin/env python3
"""
This module defines a function to calculate the sum of a list of floating-point numbers.

Functions:
    sum_list(input_list: List[float]) -> float:
        Returns the total sum of all float elements in the given list.
"""


from typing import List
def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list containing floating-point numbers.

    Returns:
        float: The sum of all floats in the list.
    """
    result = input_list
    return sum(result)
