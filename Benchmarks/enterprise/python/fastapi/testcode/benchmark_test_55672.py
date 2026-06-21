# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest55672(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = await fetch_payload()
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
