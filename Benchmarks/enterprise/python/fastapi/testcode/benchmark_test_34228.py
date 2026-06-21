# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import asyncio
from app_runtime import db


async def BenchmarkTest34228(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = await fetch_payload()
    async def _evasion_task():
        requests.get(str(data))
    await _evasion_task()
    return {"updated": True}
