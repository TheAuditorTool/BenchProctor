# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest47751(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = await fetch_payload()
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
