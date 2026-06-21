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

async def BenchmarkTest42741(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
