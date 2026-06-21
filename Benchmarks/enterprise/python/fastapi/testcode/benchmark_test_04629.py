# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest04629(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ensure_str(multipart_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
