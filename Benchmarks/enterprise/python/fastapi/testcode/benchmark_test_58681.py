# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest58681(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
