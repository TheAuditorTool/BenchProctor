# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import asyncio


async def BenchmarkTest02540(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = await fetch_payload()
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
