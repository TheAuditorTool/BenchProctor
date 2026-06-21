# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


def to_text(value):
    return str(value).strip()
_shared_counter_lock = threading.Lock()

async def BenchmarkTest08978(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
