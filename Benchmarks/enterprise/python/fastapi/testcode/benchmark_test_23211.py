# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import defusedxml.ElementTree


async def BenchmarkTest23211(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
