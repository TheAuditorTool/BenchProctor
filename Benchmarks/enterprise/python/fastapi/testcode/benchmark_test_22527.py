# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import defusedxml.ElementTree


async def BenchmarkTest22527(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = await fetch_payload()
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
