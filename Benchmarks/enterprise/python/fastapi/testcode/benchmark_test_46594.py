# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


async def BenchmarkTest46594(request: Request):
    referer_value = request.headers.get('referer', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(referer_value).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
