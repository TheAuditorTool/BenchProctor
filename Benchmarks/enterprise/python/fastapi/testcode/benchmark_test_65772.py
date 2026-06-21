# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest65772(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = (lambda v: v.strip())(forwarded_ip)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
