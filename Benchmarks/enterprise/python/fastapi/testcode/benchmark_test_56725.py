# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import asyncio
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest56725(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
