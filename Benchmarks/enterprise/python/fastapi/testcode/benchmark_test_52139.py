# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest52139(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    globals()['counter'] = int(data)
    return {"updated": True}
