#!/usr/bin/env python3
'''
This module contains a function that waits for a random delay between 0,
and returns the duration of the delay.
'''


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Parameters:
    max_delay (int): The maximum number of seconds to wait.
    n (int): the number of looops

    Returns:
    list: The actual duration of the delay.
    '''
    code_start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - code_start) / n
