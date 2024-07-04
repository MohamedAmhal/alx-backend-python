#!/usr/bin/env python3
'''
creating a type floor
'''

import math
from typing import NewType
nono = NewType('nono', float)


def floor(n: nono) -> int:
    '''
    function parameters:
    n:float
    '''
    return math.floor(n)
