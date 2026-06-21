# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import tempfile


async def BenchmarkTest25048(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = await fetch_payload()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
