# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


def relay_value(value):
    return value

async def BenchmarkTest35206(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = relay_value(auth_header)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
