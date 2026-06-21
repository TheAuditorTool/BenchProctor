# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import time


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest62153(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
