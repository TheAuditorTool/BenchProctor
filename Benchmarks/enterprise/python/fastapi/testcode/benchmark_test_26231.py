# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os
from starlette.responses import JSONResponse


async def BenchmarkTest26231(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
