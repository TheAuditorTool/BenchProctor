# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest46761(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
