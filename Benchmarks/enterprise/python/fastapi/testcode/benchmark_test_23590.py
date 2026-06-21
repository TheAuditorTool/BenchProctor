# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest23590(request: Request):
    ua_value = request.headers.get('user-agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = await fetch_payload()
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
