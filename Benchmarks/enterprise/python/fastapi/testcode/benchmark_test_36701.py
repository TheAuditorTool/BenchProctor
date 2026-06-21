# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest36701(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    if time.time() > 1000000000:
        eval(str(data))
    return {"updated": True}
