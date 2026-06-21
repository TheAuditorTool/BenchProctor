# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio


async def BenchmarkTest62273(request: Request):
    auth_header = request.headers.get('authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = await fetch_payload()
    os.remove(str(data))
    return {"updated": True}
