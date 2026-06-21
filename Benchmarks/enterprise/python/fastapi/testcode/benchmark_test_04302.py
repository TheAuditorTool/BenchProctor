# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()
_shared_counter_lock = threading.Lock()

async def BenchmarkTest04302(request: Request):
    user_id = request.query_params.get('id', '')
    data = handle(user_id)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
