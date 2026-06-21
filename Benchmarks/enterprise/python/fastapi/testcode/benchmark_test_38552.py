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

async def BenchmarkTest38552(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = RequestPayload(ua_value).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
