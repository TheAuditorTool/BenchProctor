# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest73719(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
