# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


async def BenchmarkTest48693(request: Request):
    origin_value = request.headers.get('origin', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(origin_value).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
