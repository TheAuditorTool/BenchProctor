# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import os
from starlette.responses import JSONResponse


async def BenchmarkTest81303(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    random.seed(int(env_value) if str(env_value).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
