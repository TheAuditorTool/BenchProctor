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

async def BenchmarkTest58633(request: Request):
    host_value = request.headers.get('host', '')
    data = handle(host_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
