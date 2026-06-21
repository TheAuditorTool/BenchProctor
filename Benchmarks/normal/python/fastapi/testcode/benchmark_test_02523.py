# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest02523(request: Request):
    auth_header = request.headers.get('authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return {"updated": True}
