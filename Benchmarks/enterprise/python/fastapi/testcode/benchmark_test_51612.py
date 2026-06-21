# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import asyncio
from app_runtime import db


async def BenchmarkTest51612(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = await fetch_payload()
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
