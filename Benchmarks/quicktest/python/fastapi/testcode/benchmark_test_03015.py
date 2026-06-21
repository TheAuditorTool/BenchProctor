# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


request_state: dict[str, str] = {}
_shared_counter_lock = threading.Lock()

async def BenchmarkTest03015(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
