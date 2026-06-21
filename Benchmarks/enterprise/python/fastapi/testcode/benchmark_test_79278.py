# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest79278(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    int(str(data))
    return {"updated": True}
