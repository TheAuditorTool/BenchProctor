# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest13227(request: Request):
    path_value = request.path_params.get('id', '')
    ctx = RequestContext(path_value)
    data = ctx.payload
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
