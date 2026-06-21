# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest20846(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    async def _evasion_task():
        return HTMLResponse('<div>' + str(data) + '</div>')
    return await _evasion_task()
