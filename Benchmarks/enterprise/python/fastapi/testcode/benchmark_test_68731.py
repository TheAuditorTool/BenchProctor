# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
import unicodedata


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest68731(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = RequestPayload(ua_value).value
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HTMLResponse('<p>' + normalized + '</p>')
