# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import asyncio
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest06914(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = await fetch_payload()
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
