# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest58192(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
