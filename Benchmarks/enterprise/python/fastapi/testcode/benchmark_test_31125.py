# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import re
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest31125(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
