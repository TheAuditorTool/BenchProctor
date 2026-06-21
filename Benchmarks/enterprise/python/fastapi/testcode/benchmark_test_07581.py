# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest07581(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    processed = str(data).replace("<script", "")
    return HTMLResponse('<div>' + str(processed) + '</div>')
