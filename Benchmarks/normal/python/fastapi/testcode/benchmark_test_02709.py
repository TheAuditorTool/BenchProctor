# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest02709(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id}'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
