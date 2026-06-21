# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest57677(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    os.remove(str(env_value))
    return {"updated": True}
