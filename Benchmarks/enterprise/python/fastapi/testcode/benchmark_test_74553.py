# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest74553(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(env_value))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
