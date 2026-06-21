# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import asyncio


async def BenchmarkTest09753(request: Request):
    ua_value = request.headers.get('user-agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = await fetch_payload()
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
