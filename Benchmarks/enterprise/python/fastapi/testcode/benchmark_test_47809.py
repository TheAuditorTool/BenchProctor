# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest47809(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    exec(str(data))
    return {"updated": True}
