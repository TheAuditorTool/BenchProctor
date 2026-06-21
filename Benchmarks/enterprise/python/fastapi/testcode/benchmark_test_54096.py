# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest54096(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
