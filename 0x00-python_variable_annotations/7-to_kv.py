#!/usr/bin/env python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    this will take a string k and an interger
    of flat v and run both as a tuple the k must be
    the first element of the tuple and the element
    is the square of the int or float
    """
    return (k, float(v**2))
