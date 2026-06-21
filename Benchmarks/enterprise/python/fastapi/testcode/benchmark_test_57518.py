# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest57518(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    if str(data) in ('localhost', 'internal-gateway'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
