# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest56773(request: Request):
    origin_value = request.headers.get('origin', '')
    data = coalesce_blank(origin_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
