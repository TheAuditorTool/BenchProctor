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

async def BenchmarkTest80734(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
