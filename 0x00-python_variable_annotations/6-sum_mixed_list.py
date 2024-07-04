#!/usr/bin/env python3
'''
this is the function that sum all items integers and floats
'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    parameters :
    @mxd_lst : int and float mixing
    '''
    return sum(mxd_lst)
