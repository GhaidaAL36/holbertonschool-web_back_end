#!/usr/bin/env python3
"""
type-annotated function takes
string and int/float
and returns tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k
    and the square of v as a float
    """
    return (k, float(v * v))
