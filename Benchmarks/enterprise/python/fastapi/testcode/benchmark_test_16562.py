# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import asyncio
from app_runtime import db


async def BenchmarkTest16562(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return profile_value
    data = await fetch_payload()
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
