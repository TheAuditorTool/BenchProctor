# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
import asyncio


async def BenchmarkTest39784(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
