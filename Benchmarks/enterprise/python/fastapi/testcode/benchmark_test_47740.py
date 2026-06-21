# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest47740(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
