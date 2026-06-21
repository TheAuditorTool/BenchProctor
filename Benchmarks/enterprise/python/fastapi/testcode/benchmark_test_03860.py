# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
from app_runtime import auth_check


async def BenchmarkTest03860(request: Request):
    ua_value = request.headers.get('user-agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = await fetch_payload()
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
