# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest64293(request: Request):
    user_id = request.query_params.get('id', '')
    data = ensure_str(user_id)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
