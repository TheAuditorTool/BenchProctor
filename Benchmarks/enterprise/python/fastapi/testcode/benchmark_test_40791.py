# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import urllib.request


async def BenchmarkTest40791(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
