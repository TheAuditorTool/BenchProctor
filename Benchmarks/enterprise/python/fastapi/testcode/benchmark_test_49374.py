# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form
import asyncio


async def BenchmarkTest49374(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
