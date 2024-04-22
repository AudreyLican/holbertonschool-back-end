#!/usr/bin/env python3
"""Function make_multiplier, take a float 'multiplier' 
and returns a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float   ], float]:
    def multiplier_func(a: float) -> float:
        return a * multiplier
    return multiplier_func
