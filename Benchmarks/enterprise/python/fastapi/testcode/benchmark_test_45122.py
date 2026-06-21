# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest45122(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = RequestPayload(forwarded_ip).value
    importlib.import_module(str(data))
    return {"updated": True}
