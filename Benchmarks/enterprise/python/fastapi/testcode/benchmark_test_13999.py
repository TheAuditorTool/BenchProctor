# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest13999(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = RequestPayload(upload_name).value
    try:
        result = int(str(data))
    except ValueError as e:
        return JSONResponse({'error': str(e)}, status_code=400)
    return {"updated": True}
