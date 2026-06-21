# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import defusedxml.ElementTree


async def BenchmarkTest39339(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
