#!/usr/bin/env python3
"""
Module that measures the runtime of async comprehensions
"""

import asyncio
import time
from typing import Callable

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous coroutine that executes async_comprehension four times
    in parallel using asyncio.gather and measures the total runtime.

    Returns:
        The total runtime in seconds
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
