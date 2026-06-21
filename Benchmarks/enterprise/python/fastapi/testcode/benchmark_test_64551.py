# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os
import asyncio


async def BenchmarkTest64551(request: Request):
    auth_header = request.headers.get('authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = await fetch_payload()
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
