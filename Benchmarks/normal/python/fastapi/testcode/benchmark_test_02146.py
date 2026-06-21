# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


_shared_counter_lock = threading.Lock()

async def BenchmarkTest02146(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
