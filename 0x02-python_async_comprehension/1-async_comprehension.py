#!/usr/bin/env python3
'''
define the functiobs of async generator !
be be be be be eb eb ebe
'''


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    no parameters for this function
    Return :
    the runtime of the function!!
    '''
    return [_ async for _ in async_generator()]
