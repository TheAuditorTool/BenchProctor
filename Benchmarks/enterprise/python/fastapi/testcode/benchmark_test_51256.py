# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest51256(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
