# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest38731(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
