# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time
import asyncio
from app_runtime import db


async def BenchmarkTest60700(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = await fetch_payload()
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
