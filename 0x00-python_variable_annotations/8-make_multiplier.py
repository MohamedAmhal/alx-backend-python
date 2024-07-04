#!/usr/bin/env python3
'''
documentation !!
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    documentation !!!
    '''
    return lambda x: multiplier * x
