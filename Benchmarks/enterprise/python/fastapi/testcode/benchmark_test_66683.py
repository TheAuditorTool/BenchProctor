# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import asyncio


async def BenchmarkTest66683(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    if time.time() > 1000000000:
        eval(str(data))
    return {"updated": True}
