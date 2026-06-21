# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest69167(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
