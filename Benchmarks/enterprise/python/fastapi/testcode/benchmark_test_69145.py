# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest69145(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
