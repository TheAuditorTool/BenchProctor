# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw
_shared_counter_lock = threading.Lock()

async def BenchmarkTest39407(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
