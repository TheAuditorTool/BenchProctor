# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw
_shared_counter_lock = threading.Lock()

async def BenchmarkTest00140(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = RequestPayload(raw_body).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
