# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest24544(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JSONResponse({'error': 'zero division'}, status_code=400)
    result = 100 / divisor
    return {"updated": True}
