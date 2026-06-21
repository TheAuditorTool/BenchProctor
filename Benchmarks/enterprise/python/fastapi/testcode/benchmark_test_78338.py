# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest78338(request: Request):
    host_value = request.headers.get('host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
