# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import asyncio
from app_runtime import db


async def BenchmarkTest14876(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = await fetch_payload()
    async def _evasion_task():
        return HTMLResponse('<img src="' + str(data) + '">')
    return await _evasion_task()
