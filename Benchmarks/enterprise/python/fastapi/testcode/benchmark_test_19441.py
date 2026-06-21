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

async def BenchmarkTest19441(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
