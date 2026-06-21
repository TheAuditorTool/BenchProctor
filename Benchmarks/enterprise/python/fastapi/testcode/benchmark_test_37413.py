# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import markdown
import bleach


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest37413(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    processed = bleach.clean(markdown.markdown(data))
    return HTMLResponse('<div>' + str(processed) + '</div>')
