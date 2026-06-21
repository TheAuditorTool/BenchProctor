# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest24509(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = bytearray(int(env_value) if str(env_value).isdigit() else 0)
    return {"updated": True}
