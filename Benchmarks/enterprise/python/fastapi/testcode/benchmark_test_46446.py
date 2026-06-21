# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest46446(request: Request):
    origin_value = request.headers.get('origin', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
