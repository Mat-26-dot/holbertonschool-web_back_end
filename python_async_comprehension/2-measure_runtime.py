#!/usr/bin/env python3


from async_comprehension import async_comprehension
import asyncio
import time

def measure_runtime():
    
    start_time = time.perf_counter()
    end_time = time.perf_counter()
    total_time = end_time - start_time
    results = asyncio.gather(async_comprehension)
    return results
