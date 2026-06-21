# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest26084(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
