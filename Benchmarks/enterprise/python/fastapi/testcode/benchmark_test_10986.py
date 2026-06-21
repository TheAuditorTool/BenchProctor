# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import defusedxml.ElementTree


async def BenchmarkTest10986(request: Request):
    auth_header = request.headers.get('authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = await fetch_payload()
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
