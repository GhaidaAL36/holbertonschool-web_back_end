#!/usr/bin/env python3
"""
type-annotated function return sum of
integers and floats list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes integers and floats
    and returns the sum ad float
    """
    return sum(mxd_lst)
