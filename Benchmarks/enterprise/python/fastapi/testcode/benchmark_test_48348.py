# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest48348(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
