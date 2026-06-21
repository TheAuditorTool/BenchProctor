# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import base64
from starlette.responses import JSONResponse
import os


async def BenchmarkTest10945(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
