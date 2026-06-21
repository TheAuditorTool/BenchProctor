# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest11018(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
