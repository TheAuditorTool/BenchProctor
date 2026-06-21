# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest28183(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
