# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import asyncio


async def BenchmarkTest41544(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    logging.info('User action: ' + str(data))
    return {"updated": True}
