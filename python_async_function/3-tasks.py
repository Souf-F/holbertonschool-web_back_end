#!/usr/bin/env python3
"""
Module that creates asyncio tasks
"""

import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that wraps wait_random.

    Args:
        max_delay: Maximum delay for wait_random

    Returns:
        An asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
