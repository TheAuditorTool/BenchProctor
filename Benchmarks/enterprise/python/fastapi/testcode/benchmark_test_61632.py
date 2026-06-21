# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest61632(request: Request):
    upload_name = (await request.form()).get('upload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = await fetch_payload()
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
