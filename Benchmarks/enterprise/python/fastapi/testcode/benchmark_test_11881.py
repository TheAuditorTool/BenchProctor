# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest11881(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = RequestPayload(raw_body).value
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
