#!/usr/bin/env python3
"""
0. The basics of async
"""
import asyncio, random


async def wait_random(max_delay: int = 10):
    """
    wait between random valeu
    and max_delay value
    """
    random_value = random.uniform(0, max_delay)
    await asyncio.sleep(random_value)
    return random_value
