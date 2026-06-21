# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest13528(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
