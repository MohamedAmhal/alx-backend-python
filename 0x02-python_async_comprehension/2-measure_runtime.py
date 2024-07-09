#!/usr/bin/env python3
'''
define the functiobs of async generator !
be be be be be eb eb ebe
'''


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    no parameters for this function
    Return :
    the runtime of the function!!
    '''
    start_code = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_code
