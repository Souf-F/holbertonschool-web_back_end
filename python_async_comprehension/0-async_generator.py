#!/usr/bin/env python3
"""
Module that contains an asynchronous generator
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that loops 10 times, asynchronously waits
    1 second each time, and yields a random number between 0 and 10.

    Yields:
        A random float between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
