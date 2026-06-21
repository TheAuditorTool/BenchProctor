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

async def BenchmarkTest45369(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
