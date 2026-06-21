# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import db


async def BenchmarkTest09521(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = await fetch_payload()
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
