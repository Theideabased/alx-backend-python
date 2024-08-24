#!/usr/bin/env python3
import asyncio
import random


"""
This code will def a function that will accept an integer
then it will be delayed be a random number from 0 to the
valur inputted then it will be printed
"""


async def wait_random(max_delay: int = 10) -> float:
    """ the input must be an integer variable and
    a default value of 10 then then a random value
    from 0 to max_delay so that it will be delayed
    by the random number that is choosen
    """
    time_to_delay = random.uniform(0, max_delay)
    await asyncio.sleep(time_to_delay)
    return time_to_delay
asyncio.run(wait_random())
