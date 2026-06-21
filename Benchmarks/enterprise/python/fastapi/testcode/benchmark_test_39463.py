# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest39463(request: Request):
    host_value = request.headers.get('host', '')
    data = handle(host_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    return HTMLResponse(str(processed))
