# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio


async def BenchmarkTest20954(request: Request):
    auth_header = request.headers.get('authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = await fetch_payload()
    processed = data[:64]
    request.session['data'] = str(processed)
    return {"updated": True}
