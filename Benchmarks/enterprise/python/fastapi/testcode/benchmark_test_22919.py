# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest22919(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
