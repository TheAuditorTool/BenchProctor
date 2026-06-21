# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest45207(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
