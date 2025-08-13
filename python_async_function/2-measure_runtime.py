#!/usr/bin/env python3
"""Measure the average execution time per coroutine."""

from concurrent_coroutines import wait_n
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine."""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    """Returns:
        float: Average execution time per coroutine in seconds.
    """
    return total_time / n
