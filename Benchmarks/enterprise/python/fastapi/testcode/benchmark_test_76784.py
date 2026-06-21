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

async def BenchmarkTest76784(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
