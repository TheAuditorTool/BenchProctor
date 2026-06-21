# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os


request_state: dict[str, str] = {}

async def BenchmarkTest29687(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
