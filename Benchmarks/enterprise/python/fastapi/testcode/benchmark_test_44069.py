# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest44069(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
