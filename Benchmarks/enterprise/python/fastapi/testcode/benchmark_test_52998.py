# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest52998(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
