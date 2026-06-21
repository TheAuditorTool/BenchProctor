# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import asyncio
import importlib


async def BenchmarkTest49071(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = await fetch_payload()
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return {"updated": True}
