# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import asyncio


_shared_counter_lock = threading.Lock()

async def BenchmarkTest61081(request: Request):
    origin_value = request.headers.get('origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = await fetch_payload()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
