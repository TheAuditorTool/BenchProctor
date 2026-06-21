# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


async def BenchmarkTest69017(request: Request):
    ua_value = request.headers.get('user-agent', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(ua_value).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
