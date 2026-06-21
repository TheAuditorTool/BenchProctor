# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import asyncio


_shared_counter_lock = threading.Lock()

async def BenchmarkTest19228(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = await fetch_payload()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
