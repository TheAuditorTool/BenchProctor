# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import tempfile


async def BenchmarkTest06698(request: Request):
    origin_value = request.headers.get('origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = await fetch_payload()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
