#!/usr/bin/env python3
"""Function make_multiplier, take a float 'multiplier' 
and returns a function that multiplies a float by multiplier"""
from typing import Tuple, Iterable, List


def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]
