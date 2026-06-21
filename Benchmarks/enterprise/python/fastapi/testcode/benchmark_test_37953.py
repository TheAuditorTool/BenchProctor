# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest37953(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
