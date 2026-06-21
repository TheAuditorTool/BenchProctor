# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest00384(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    with _shared_counter_lock:
        globals()['counter'] = int(cookie_value)
    return {"updated": True}
