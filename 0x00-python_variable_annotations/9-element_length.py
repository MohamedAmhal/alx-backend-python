#!/usr/bin/env python3
'''
documentation !!!
'''


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    documentation !!!
    '''
    return [(i, len(i)) for i in lst]
