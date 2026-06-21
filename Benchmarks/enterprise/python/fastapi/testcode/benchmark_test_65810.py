# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import asyncio


_shared_counter_lock = threading.Lock()

async def BenchmarkTest65810(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
