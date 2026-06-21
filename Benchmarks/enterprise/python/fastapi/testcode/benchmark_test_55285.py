# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import asyncio


async def BenchmarkTest55285(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    globals()['counter'] = int(data)
    return {"updated": True}
