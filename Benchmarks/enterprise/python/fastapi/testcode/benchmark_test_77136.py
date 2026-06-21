# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import JSONResponse
import os


async def BenchmarkTest77136(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
