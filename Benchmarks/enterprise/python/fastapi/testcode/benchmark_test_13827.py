# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import re
from starlette.responses import JSONResponse
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest13827(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    globals()['counter'] = int(processed)
    return {"updated": True}
