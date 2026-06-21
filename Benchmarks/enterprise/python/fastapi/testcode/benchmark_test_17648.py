# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest17648(request: Request):
    origin_value = request.headers.get('origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = await fetch_payload()
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
