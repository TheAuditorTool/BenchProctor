# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import db


async def BenchmarkTest25679(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    async def _evasion_task():
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    await _evasion_task()
    return {"updated": True}
