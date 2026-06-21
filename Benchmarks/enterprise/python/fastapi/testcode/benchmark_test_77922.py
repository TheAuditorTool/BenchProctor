# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest77922(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
