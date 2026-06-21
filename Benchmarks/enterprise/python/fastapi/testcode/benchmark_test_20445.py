# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw
_shared_counter_lock = threading.Lock()

async def BenchmarkTest20445(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
