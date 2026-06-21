# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


async def BenchmarkTest64297(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(multipart_value).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
