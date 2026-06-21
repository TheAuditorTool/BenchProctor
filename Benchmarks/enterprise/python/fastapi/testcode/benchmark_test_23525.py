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

async def BenchmarkTest23525(request: Request):
    host_value = request.headers.get('host', '')
    data = handle(host_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
