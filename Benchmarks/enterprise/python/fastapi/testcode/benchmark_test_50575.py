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

async def BenchmarkTest50575(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
