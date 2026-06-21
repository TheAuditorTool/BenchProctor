# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest57370(request: Request):
    host_value = request.headers.get('host', '')
    data = RequestPayload(host_value).value
    importlib.import_module(str(data))
    return {"updated": True}
