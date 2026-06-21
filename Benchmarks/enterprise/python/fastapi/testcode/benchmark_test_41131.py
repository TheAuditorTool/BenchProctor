# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest41131(request: Request):
    referer_value = request.headers.get('referer', '')
    data = RequestPayload(referer_value).value
    request.session['data'] = str(data)
    return {"updated": True}
