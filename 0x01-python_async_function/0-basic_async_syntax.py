#!/usr/bin/env python3
"""
This module contains a function that waits for a random delay between 0,
and returns the duration of the delay.
"""


import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay between 0 and max_delay
    (inclusive) seconds and returns the delay.

    Parameters:
    max_delay (float): The maximum number of seconds to wait.
    Defaults to 10 seconds.

    Returns:
    float: The actual duration of the delay.
    """
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
