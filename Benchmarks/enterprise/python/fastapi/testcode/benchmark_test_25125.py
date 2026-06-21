# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import json
from starlette.responses import JSONResponse
import os


async def BenchmarkTest25125(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
