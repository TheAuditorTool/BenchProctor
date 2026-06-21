# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest29642(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = await fetch_payload()
    if str(data) == 'fluffy':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
