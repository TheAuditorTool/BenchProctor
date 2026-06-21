# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest33135(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if not str(env_value).isdigit():
        raise ValueError('invalid input: ' + str(env_value))
    return {"updated": True}
