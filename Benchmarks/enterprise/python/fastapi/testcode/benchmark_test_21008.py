# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from fastapi import Form
from starlette.responses import JSONResponse
import os


async def BenchmarkTest21008(request: Request, field: str = Form('')):
    field_value = field
    digest = hashlib.pbkdf2_hmac('sha256', str(field_value).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
