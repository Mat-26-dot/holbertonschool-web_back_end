#!/usr/bin/env python3

from async_generator import async_generator
import asyncio
import random

async def async_comprehension() -> float:
        results = [item async for item in async_generator()]
        return(results)