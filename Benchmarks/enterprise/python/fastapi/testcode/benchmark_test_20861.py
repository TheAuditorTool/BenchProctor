# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest20861(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
