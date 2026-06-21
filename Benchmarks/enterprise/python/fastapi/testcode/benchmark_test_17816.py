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

async def BenchmarkTest17816(request: Request):
    user_id = request.query_params.get('id', '')
    data = handle(user_id)
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
