# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest11708(request: Request):
    referer_value = request.headers.get('referer', '')
    data = RequestPayload(referer_value).value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
