# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest03243(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
