# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest56814(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if str(data).startswith(('10.', '192.168.', '127.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
