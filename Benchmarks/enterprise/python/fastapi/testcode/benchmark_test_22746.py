# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from types import SimpleNamespace
from app_runtime import db


_shared_counter_lock = threading.Lock()

async def BenchmarkTest22746(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
