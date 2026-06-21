# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import time
import asyncio


async def BenchmarkTest62635(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    if time.time() > 1000000000:
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
