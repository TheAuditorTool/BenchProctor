# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


_shared_counter_lock = threading.Lock()

async def BenchmarkTest54173(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with _shared_counter_lock:
        globals()['counter'] = int(comment_value)
    return {"updated": True}
