#!/usr/bin/env python3
'''
this is the function that sun all ites in a liste
'''


from typing import TypeAlias
liste: TypeAlias = list[float]


def sum_list(input_list: liste) -> float:
    '''
    parameters:
    @input_list : the list value
    '''

    return sum(input_list)
