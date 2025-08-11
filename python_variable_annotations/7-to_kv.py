#!/usr/bin/env python3
"""This module to_kv takes a string, int or float as args
and returns a tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """the square root of the tuple value was returned"""
    return (k, float(v**2))
