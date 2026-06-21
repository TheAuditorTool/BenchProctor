# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse
import subprocess


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest80971(request: Request):
    host_value = request.headers.get('host', '')
    data = RequestPayload(host_value).value
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
