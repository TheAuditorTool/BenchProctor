# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()
_shared_counter_lock = threading.Lock()

async def BenchmarkTest31786(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
