#!/usr/bin/env python3
"""
    Return a list of tuples containing each element from the input iterable
    and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence-like objects
            (e.g., strings, lists, tuples) where each element supports len().

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        the original element and an integer representing its length."""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
