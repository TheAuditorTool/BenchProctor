# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import os
from starlette.responses import JSONResponse


async def BenchmarkTest41821(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    random.seed(int(env_value) if str(env_value).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
