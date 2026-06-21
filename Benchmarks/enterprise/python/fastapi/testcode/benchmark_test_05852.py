# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio


async def BenchmarkTest05852(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    processed = data[:64]
    os.system('echo ' + str(processed))
    return {"updated": True}
