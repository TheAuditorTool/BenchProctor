# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest55487(request: Request):
    upload_name = (await request.form()).get('upload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = await fetch_payload()
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
