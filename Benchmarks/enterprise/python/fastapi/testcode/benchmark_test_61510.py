# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json


_shared_counter_lock = threading.Lock()

async def BenchmarkTest61510(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
