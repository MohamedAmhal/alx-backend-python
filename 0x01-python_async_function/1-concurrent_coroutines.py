#!/usr/bin/env python3
'''
This module contains a function that waits for a random delay between 0,
and returns the duration of the delay.
'''


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Parameters:
    max_delay (int): The maximum number of seconds to wait.
    n (int): the number of looops

    Returns:
    list: The actual duration of the delay.
    '''

    lilo = []
    for i in range(n):
        lilo.append(wait_random(max_delay))

    r = await asyncio.gather(*lilo)

    return sorted(r)
