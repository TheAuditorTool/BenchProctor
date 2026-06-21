# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json


_shared_counter_lock = threading.Lock()

async def BenchmarkTest57390(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
