# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import asyncio
from app_runtime import db


async def BenchmarkTest51075(request: Request):
    ua_value = request.headers.get('user-agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = await fetch_payload()
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
