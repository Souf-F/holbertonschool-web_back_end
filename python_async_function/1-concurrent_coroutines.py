#!/usr/bin/env python3
"""
Module that contains a coroutine that executes multiple coroutines concurrently
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the
    specified max_delay and returns the list of all delays in ascending order.

    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay for each wait_random call

    Returns:
        A list of all delays in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
