# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest69840(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
