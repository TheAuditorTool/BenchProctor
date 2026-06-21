# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import asyncio


async def BenchmarkTest31216(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = await fetch_payload()
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    await _evasion_task()
    return {"updated": True}
