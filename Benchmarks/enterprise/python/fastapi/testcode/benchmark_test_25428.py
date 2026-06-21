# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest25428(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    os.remove(str(env_value))
    return {"updated": True}
