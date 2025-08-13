#!/usr/bin/env python3
"""This module creates and returns a asyncio Task that
runs wait_random with the given max_delay."""
from basic_async_syntax import wait_random

import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task that runs wait_random with
    the given max_delay.

    Args:
        max_delay (int): Maximum number of seconds to wait.

    Returns:
        asyncio.Task: A scheduled task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
