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

async def BenchmarkTest10689(request: Request):
    referer_value = request.headers.get('referer', '')
    data = RequestPayload(referer_value).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
