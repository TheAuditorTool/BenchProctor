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

async def BenchmarkTest08478(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    os.seteuid(65534)
    return {"updated": True}
