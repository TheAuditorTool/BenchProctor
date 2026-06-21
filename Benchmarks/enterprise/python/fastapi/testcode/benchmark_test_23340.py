# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
from app_runtime import db


async def BenchmarkTest23340(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = await fetch_payload()
    if os.environ.get("APP_ENV", "production") != "test":
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
