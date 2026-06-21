# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json


_shared_counter_lock = threading.Lock()

async def BenchmarkTest09640(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
