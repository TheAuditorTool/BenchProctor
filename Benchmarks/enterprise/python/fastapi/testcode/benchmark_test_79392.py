# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


_shared_counter_lock = threading.Lock()

async def BenchmarkTest79392(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
