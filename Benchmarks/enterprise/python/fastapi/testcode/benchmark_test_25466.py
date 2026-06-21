# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import requests


async def BenchmarkTest25466(request: Request):
    origin_value = request.headers.get('origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = await fetch_payload()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
