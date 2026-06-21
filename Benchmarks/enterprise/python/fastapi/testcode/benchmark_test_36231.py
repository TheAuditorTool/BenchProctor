# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest36231(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
