# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest02482(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
