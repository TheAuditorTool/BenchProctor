# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import asyncio
from app_runtime import auth_check


async def BenchmarkTest79329(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
