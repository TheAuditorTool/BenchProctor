# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


class RequestContext:
    def __init__(self, payload):
        self.payload = payload
_shared_counter_lock = threading.Lock()

async def BenchmarkTest57140(request: Request):
    origin_value = request.headers.get('origin', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
