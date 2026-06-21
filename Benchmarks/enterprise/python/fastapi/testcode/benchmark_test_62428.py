# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time
import asyncio


async def BenchmarkTest62428(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = await fetch_payload()
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
