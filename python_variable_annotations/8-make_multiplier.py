#!/usr/bin/env python3
"""
    Creates a multiplier function that multiplies its
    input by a fixed multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(value: float) -> float:
        """Args:
                multiplier (float): The number to multiply inputs by."""

        return value * multiplier
    return multiplier_function


"""Returns:
        Callable[[float], float]: A function that takes a float
        and returns the product of that float and the multiplier.
    """
