# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


async def BenchmarkTest13787(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(header_value).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
