#!/usr/bin/env python3
'''
the first task that return a random value in seconds
'''

import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    '''
    documentations
    parameters:
    @max_deplay : the maximum of seconds
    '''
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
