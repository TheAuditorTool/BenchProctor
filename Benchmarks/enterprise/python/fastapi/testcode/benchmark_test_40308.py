# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest40308(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = await fetch_payload()
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
