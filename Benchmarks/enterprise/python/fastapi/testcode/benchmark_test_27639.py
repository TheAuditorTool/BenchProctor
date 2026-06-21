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

async def BenchmarkTest27639(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = handle(forwarded_ip)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
