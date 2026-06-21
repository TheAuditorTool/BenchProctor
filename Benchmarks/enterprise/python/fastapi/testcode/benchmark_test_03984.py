# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import os
from starlette.responses import JSONResponse


async def BenchmarkTest03984(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
