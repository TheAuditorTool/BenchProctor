# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import asyncio


_shared_counter_lock = threading.Lock()

async def BenchmarkTest03820(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
