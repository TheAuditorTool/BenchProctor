# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


request_state: dict[str, str] = {}
_shared_counter_lock = threading.Lock()

async def BenchmarkTest61535(request: Request):
    upload_name = (await request.form()).get('upload', '')
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
