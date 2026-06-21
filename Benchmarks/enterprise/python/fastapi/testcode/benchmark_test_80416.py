# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import asyncio


async def BenchmarkTest80416(request: Request):
    auth_header = request.headers.get('authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = await fetch_payload()
    if time.time() > 1000000000:
        eval(str(data))
    return {"updated": True}
