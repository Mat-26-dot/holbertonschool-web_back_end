#!/usr/bin/env python3
"""
Calculate the sum of a list containing both integers and floats.

Args:
    mxd_lst (List[Union[int, float]]): A list of numbers,
        where each element can be either an integer or a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Called the function by using result as a variable"""
    result = mxd_lst
    """Returns:
        float: The total sum of all numbers in the list,
        returned as a float."""
    return sum(result)
