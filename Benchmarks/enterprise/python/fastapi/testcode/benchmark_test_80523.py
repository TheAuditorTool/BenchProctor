# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest80523(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    def _primary():
        return HTMLResponse('<img src="' + str(data) + '">')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
