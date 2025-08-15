#!/usr/bin/env python3
"""This module collects 10 random nums and returns 10 random nums"""

from async_generator import async_generator
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """this function collects 10 random nums"""
    results = [item async for item in async_generator()]
    """the function is called through a variable to return the func"""
    return (results)
