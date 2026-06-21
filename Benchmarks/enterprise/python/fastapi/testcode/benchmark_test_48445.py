# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest48445(request: Request):
    referer_value = request.headers.get('referer', '')
    data = RequestPayload(referer_value).value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
