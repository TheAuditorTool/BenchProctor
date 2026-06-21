# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest24368(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    if str(data) == 'is_admin':
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
