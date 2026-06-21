# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest15377(request: Request):
    origin_value = request.headers.get('origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = await fetch_payload()
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
