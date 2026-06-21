# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import os
import asyncio


async def BenchmarkTest58104(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = await fetch_payload()
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    return {"updated": True}
