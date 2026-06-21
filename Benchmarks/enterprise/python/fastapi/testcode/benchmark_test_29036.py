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

async def BenchmarkTest29036(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
