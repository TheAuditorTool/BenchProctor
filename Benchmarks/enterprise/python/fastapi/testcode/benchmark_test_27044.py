# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import asyncio


async def BenchmarkTest27044(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    async def _evasion_task():
        return HTMLResponse('<img src="' + str(data) + '">')
    return await _evasion_task()
