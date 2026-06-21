# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import asyncio


async def BenchmarkTest47355(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = await fetch_payload()
    async def _evasion_task():
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    return await _evasion_task()
