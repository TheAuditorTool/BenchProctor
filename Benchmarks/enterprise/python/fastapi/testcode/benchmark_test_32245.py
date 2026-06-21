# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest32245(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = RequestPayload(ua_value).value
    globals()['counter'] = int(data)
    return {"updated": True}
