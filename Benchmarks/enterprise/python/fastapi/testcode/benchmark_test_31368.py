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

async def BenchmarkTest31368(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = RequestPayload(auth_header).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
