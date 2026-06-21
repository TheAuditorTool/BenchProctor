# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio


async def BenchmarkTest81207(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return {"updated": True}
