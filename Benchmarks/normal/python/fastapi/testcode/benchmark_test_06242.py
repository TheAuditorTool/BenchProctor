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

async def BenchmarkTest06242(request: Request):
    user_id = request.query_params.get('id', '')
    data = RequestPayload(user_id).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
