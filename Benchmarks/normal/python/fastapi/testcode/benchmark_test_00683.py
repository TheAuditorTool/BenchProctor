# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest00683(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
