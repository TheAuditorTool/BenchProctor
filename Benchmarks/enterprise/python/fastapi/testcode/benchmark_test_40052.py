# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import db


async def BenchmarkTest40052(request: Request):
    ua_value = request.headers.get('user-agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = await fetch_payload()
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
