# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest27917(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
