#!/usr/bin/env python3


from async_comprehension import async_comprehension
import asyncio
import time

async def measure_runtime() -> float:
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
    async_comprehension(), async_comprehension())
    """so this lets it run simultaneously 4 times"""
    end_time = time.perf_counter()
    total_time =  start_time = end_time - start_time
    return end_time - start_time