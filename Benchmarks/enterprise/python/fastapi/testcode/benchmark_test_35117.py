# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


async def BenchmarkTest35117(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(cookie_value).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
