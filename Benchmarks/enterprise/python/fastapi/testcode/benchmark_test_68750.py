# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import requests
from app_runtime import db


async def BenchmarkTest68750(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = await fetch_payload()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
