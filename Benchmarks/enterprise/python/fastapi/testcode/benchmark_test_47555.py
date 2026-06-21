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

async def BenchmarkTest47555(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
