# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import asyncio


_shared_counter_lock = threading.Lock()

async def BenchmarkTest36675(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = await fetch_payload()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
