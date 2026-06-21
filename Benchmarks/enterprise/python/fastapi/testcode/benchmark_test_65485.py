# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest65485(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    return HTMLResponse('<img src="' + str(data) + '">')
