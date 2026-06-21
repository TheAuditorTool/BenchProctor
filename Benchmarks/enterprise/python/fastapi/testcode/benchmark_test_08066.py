# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest08066(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    os.remove(str(data))
    return {"updated": True}
