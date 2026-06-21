# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


_shared_counter_lock = threading.Lock()

async def BenchmarkTest04032(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
