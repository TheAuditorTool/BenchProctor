# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest52400(request: Request):
    path_value = request.path_params.get('id', '')
    with _shared_counter_lock:
        globals()['counter'] = int(path_value)
    return {"updated": True}
