# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest64479(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
