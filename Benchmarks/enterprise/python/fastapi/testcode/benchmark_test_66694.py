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

async def BenchmarkTest66694(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
