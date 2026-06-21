# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest16307(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = await fetch_payload()
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse(Template(processed).render())
