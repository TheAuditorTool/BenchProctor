# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
from app_runtime import db


async def BenchmarkTest62498(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = await fetch_payload()
    os.remove(str(data))
    return {"updated": True}
