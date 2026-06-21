# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import defusedxml.ElementTree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest39389(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
