# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest00751(request: Request):
    path_value = request.path_params.get('id', '')
    ctx = RequestContext(path_value)
    data = ctx.payload
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
