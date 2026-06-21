# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest30858(request: Request):
    referer_value = request.headers.get('referer', '')
    data = RequestPayload(referer_value).value
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
