# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


async def BenchmarkTest50606(request: Request):
    upload_name = (await request.form()).get('upload', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(upload_name).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
