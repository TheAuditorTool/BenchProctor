# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()
_shared_counter_lock = threading.Lock()

async def BenchmarkTest03729(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
