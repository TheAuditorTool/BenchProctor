# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import base64
from starlette.responses import JSONResponse
import os


async def BenchmarkTest48617(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
