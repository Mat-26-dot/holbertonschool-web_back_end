#!/usr/bin/env python3


from concurrent_coroutines import wait_n
import time
import asyncio

def measure_time(n: int, max_delay: int) -> float:

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time

    return total_time / n
