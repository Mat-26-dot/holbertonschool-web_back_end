#!/usr/bin/env python3
"""Module for running multiple asynchronous wait_random calls.
This module contains the async routine wait_n which calls wait_random
n times concurrently with the given maximum delay, and gathers
the delays in ascending order without explicitly sorting them."""


from basic_async_syntax import wait_random
from typing import List
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the given max_delay and return
    the list of all the delays in ascending order without using sort().

    The ascending order is achieved by using asyncio.as_completed(),
    which yields results as soon as each task is completed."""

    empty_list = []


    tasks = [asyncio.create_task(wait_random(max_delay))for i in range(n)]
    
    results = []
    for task in asyncio.as_completed(tasks):
        """The ascending order is achieved by using asyncio.as_completed(),
        which yields results as soon as each task is completed."""
        result = await task
        results.append(result)
    """Returns:
        List[float]: list of delays in ascending order.
    """
    return (results)
