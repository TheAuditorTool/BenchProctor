# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest57904(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
