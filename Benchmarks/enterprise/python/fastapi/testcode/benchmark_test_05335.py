# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest05335(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = handle(xml_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
