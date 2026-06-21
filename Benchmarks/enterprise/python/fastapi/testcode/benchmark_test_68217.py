# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest68217(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
