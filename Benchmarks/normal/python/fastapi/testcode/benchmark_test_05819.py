# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


request_state: dict[str, str] = {}
_shared_counter_lock = threading.Lock()

async def BenchmarkTest05819(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
