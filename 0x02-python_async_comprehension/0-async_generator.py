#!/usr/bin/env python3
'''
define the functiobs of async generator !
be be be be be eb eb ebe
'''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    no parameters for this function
    Return:
    a list of floats (random values between 0 and 10)
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
