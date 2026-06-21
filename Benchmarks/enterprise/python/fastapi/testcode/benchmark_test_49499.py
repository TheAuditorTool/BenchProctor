# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest49499(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        result = int(str(env_value))
    except Exception:
        pass
    return {"updated": True}
