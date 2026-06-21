# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


_shared_counter_lock = threading.Lock()

async def BenchmarkTest67133(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
