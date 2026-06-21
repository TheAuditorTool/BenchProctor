# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest48314(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
