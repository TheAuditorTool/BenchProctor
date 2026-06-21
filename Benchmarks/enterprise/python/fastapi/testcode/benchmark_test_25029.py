# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest25029(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = RequestPayload(upload_name).value
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JSONResponse({'validated': str(processed)}, status_code=200)
    return {"updated": True}
