# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import asyncio
from app_runtime import db


async def BenchmarkTest32126(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
