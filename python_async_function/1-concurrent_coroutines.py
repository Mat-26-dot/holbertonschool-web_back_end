#!/usr/bin/env python3

from basic_async_syntax import wait_random

import asyncio

async def wait_n(n: int, max_delay: float) -> int:
    
    #Step 1
    empty_list = []

    #Step 2
    tasks  = [asyncio.create_task(wait_random(max_delay))for i in range(n)]

    #Step 3
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return (results)


    



