# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import requests


async def BenchmarkTest26480(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
