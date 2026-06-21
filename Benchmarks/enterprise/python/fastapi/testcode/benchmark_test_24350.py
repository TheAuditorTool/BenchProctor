# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import os
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest24350(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
