# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest41714(request: Request):
    user_id = request.query_params.get('id', '')
    data = RequestPayload(user_id).value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
