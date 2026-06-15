#!/usr/bin/env python3
"""
Asynchronous coroutine that take a int argument
and wait a random delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine who wait for a delay"""

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
