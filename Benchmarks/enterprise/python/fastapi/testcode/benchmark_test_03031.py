# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio


async def BenchmarkTest03031(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
