# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


class RequestContext:
    def __init__(self, payload):
        self.payload = payload
_shared_counter_lock = threading.Lock()

async def BenchmarkTest03281(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
