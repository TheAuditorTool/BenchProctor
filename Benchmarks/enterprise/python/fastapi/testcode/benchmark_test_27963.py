# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio


async def BenchmarkTest27963(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    async def _evasion_task():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    await _evasion_task()
    return {"updated": True}
