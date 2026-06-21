# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import time
import asyncio


async def BenchmarkTest32107(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    if time.time() > 1000000000:
        return HTMLResponse(Template(data).render())
    return {"updated": True}
