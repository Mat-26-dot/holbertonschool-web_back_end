#!/usr/bin/env python3
"""This module will loop 10 times, each time asynchronously"""
import random
import asyncio

async def async_generator():
    """coroutine defined asynchronously"""
    for i in range(10): 
        """loop count to 10"""
        result = random.uniform(0, 10) 
        """float count count to 10"""
        await asyncio.sleep(1)
        yield result 
        """result form float count yielded"""
