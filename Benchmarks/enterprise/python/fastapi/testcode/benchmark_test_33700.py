# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio
from app_runtime import db


async def BenchmarkTest33700(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = await fetch_payload()
    processed = data[:64]
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
