# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import os
import asyncio


async def BenchmarkTest47447(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = await fetch_payload()
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
