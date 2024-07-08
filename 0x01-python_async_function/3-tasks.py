#!/usr/bin/env python3
'''
This module contains a function that waits for a random delay between 0,
and returns the duration of the delay.
'''


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Parameters:
    max_delay (int): The maximum number of seconds to wait.

    Returns:
    aysyncio.task: The actual duration of the delay.
    '''
    return asyncio.Task(wait_random(max_delay))
