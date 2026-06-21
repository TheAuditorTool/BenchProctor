# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload
_shared_counter_lock = threading.Lock()

async def BenchmarkTest06740(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
