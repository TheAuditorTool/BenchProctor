# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import defusedxml.ElementTree


async def BenchmarkTest09641(request: Request):
    upload_name = (await request.form()).get('upload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = await fetch_payload()
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
