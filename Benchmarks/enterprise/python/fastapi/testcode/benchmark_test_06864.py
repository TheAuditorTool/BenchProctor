# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest06864(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = RequestPayload(xml_value).value
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
