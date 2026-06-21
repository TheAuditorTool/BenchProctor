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

async def BenchmarkTest35357(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    processed = data[:64]
    trusted_claim = str(processed)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
