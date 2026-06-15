#!/usr/bin/env python3
"""
Module that contains a coroutine that executes multiple tasks concurrently
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times with the
    specified max_delay and returns the list of all delays in ascending order.

    Args:
        n: Number of times to spawn task_wait_random
        max_delay: Maximum delay for each task_wait_random call

    Returns:
        A list of all delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
