# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import auth_check


async def BenchmarkTest34118(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    auth_check('user', data)
    return {"updated": True}
