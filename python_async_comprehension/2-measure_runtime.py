#!/usr/bin/env python3
"""This module will execute 4 times in parallel uing asyncio.gather"""


from async_comprehension import async_comprehension
import asyncio
import time


async def measure_runtime() -> float:
    """Measure time to run async_comprehension 4 times"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    """so this lets the func run simultaneously 4 times"""
    end_time = time.perf_counter()
    """timer ends"""
    total_time = end_time - start_time
    """returns end and start time"""
    return end_time - start_time
