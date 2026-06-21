# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def relay_value(value):
    return value
_shared_counter_lock = threading.Lock()

async def BenchmarkTest33298(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
