# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest26729(request: Request):
    path_value = request.path_params.get('id', '')
    ctx = RequestContext(path_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return {"updated": True}
