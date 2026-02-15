#!/usr/bin/env python3
"""
type-annotated function return float sum
of list of float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    return the sum of float list
    """
    return sum(input_list)
