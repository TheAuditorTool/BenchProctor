# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest74995(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
