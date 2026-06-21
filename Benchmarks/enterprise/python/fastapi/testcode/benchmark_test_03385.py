# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import os
from starlette.responses import JSONResponse


async def BenchmarkTest03385(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
