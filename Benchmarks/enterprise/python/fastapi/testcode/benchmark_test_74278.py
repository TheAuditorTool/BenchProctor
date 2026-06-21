# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


async def BenchmarkTest74278(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
