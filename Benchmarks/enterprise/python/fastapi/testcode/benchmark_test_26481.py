# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import os
from starlette.responses import JSONResponse


async def BenchmarkTest26481(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
