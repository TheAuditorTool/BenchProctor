# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio
from app_runtime import db


async def BenchmarkTest76209(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = await fetch_payload()
    processed = data[:64]
    if str(processed) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
