# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import asyncio


async def BenchmarkTest20318(request: Request):
    origin_value = request.headers.get('origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = await fetch_payload()
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
