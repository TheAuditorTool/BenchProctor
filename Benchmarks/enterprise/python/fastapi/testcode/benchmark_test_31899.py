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

async def BenchmarkTest31899(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
