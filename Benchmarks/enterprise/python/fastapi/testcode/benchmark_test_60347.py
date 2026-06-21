# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest60347(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
