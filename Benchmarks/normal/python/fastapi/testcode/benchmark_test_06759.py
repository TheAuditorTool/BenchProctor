# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest06759(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ensure_str(upload_name)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
