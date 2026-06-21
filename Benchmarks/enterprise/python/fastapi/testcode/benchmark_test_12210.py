# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import html
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest12210(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    processed = str(data).replace("<script", "")
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
