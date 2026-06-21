# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest74414(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
