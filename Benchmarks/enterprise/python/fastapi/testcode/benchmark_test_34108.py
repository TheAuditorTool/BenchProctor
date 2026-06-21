# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import asyncio


async def BenchmarkTest34108(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    logging.info('User action: ' + str(data))
    return {"updated": True}
