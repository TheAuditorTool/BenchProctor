# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import asyncio


async def BenchmarkTest03046(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
