# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


async def BenchmarkTest10372(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
