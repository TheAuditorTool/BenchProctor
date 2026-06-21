# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest34663(request: Request):
    upload_name = (await request.form()).get('upload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = await fetch_payload()
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
