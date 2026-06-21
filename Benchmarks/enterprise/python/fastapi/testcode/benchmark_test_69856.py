# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest69856(request: Request):
    host_value = request.headers.get('host', '')
    data = RequestPayload(host_value).value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
