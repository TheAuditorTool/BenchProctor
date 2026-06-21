# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest79953(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
