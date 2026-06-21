# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest68478(request: Request):
    path_value = request.path_params.get('id', '')
    data = RequestPayload(path_value).value
    globals()['counter'] = int(data)
    return {"updated": True}
