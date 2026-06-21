# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest45776(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = await fetch_payload()
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
