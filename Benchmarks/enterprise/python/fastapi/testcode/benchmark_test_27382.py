# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw
_shared_counter_lock = threading.Lock()

async def BenchmarkTest27382(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
