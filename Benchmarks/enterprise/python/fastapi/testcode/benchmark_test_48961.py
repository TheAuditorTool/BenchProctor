# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio
from app_runtime import db


async def BenchmarkTest48961(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JSONResponse({'record': str(record)}, status_code=200)
