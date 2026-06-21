# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest13459(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = RequestPayload(raw_body).value
    json.loads(data)
    return {"updated": True}
