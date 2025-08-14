#!/usr/bin/env python3

from async_generator import async_generator
import asyncio
from typing import List

async def async_comprehension() -> List[float]:
        results = [item async for item in async_generator()]
        return(results)