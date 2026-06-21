# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest53313(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = RequestPayload(raw_body).value
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
