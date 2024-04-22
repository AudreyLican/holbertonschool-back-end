#!/usr/bin/env python3
"""Function to_kv, take a string 'k' and an int or a float'v'
and return a tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: List[Union[int, float]]) -> Tuple[str, float]:
    return k, float(v)**2
