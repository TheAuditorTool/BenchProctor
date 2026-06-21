# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import asyncio
from app_runtime import db


async def BenchmarkTest18005(request: Request):
    upload_name = (await request.form()).get('upload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = await fetch_payload()
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
