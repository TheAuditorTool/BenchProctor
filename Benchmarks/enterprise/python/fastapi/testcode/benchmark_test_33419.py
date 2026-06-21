# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()
_shared_counter_lock = threading.Lock()

async def BenchmarkTest33419(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = handle(db_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
