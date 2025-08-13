#!/usr/bin/env python3

from basic_async_syntax import wait_random

import asyncio

def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))