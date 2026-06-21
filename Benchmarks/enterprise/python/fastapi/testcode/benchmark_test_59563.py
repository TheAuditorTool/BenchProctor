# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio


async def BenchmarkTest59563(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
