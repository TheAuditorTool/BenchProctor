# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import db


async def BenchmarkTest64607(request: Request):
    origin_value = request.headers.get('origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = await fetch_payload()
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
