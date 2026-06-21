# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest65909(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
