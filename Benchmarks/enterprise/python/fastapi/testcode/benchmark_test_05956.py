# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import base64
from app_runtime import db


_shared_counter_lock = threading.Lock()

async def BenchmarkTest05956(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
