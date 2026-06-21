# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time
import asyncio


async def BenchmarkTest11083(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return {"updated": True}
