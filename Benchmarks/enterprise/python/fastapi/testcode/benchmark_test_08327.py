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

async def BenchmarkTest08327(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
