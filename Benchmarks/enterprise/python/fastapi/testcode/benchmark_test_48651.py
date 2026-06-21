# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


class RequestContext:
    def __init__(self, payload):
        self.payload = payload
_shared_counter_lock = threading.Lock()

async def BenchmarkTest48651(request: Request):
    referer_value = request.headers.get('referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
