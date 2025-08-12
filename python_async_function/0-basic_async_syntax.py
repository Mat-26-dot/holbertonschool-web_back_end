#!/usr/bin/env python3
""" This module takes an integer arg max_delay with 10 as its
default and wait_random waits for a random delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    delay: float = random.uniform(0, max_delay)
    """Args:
        max_delay (int): The maximum number of seconds to wait.
        Defaults to 10."""
    await asyncio.sleep(delay)
    """Returns:
        float: The actual delay time in seconds."""
    return delay
