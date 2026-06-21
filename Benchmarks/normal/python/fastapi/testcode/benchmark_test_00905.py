# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest00905(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = default_blank(header_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
