# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio


async def BenchmarkTest08000(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    os.remove(str(data))
    return {"updated": True}
