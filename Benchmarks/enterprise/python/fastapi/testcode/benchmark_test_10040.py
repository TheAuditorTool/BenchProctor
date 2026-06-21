# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import os
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest10040(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
