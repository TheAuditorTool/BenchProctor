# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest15353(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
