# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


async def BenchmarkTest33824(request: Request):
    user_id = request.query_params.get('id', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(user_id).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
