#!/usr/bin/env python3
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ This will return a list of the variables of the
    value number n times
    """
    res = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    m = len(res)
    for a in range(m):
        for b in range(m-a-1):
            if res[b] > res[b+1]:
                res[b], res[b+1] = res[b+1], res[b]
    return res
