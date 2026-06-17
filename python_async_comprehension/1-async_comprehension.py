#!/usr/bin/env python3
"""
Module that contains an asynchronous comprehension
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random numbers using
    an async comprehension over async_generator and returns them.

    Returns:
        A list of 10 random float numbers
    """
    return [i async for i in async_generator()]
