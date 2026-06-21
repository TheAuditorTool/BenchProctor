# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import asyncio


async def BenchmarkTest39801(request: Request):
    query_array = request.query_params.get('items', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return query_array
    data = await fetch_payload()
    logging.info('User action: ' + str(data))
    return {"updated": True}
