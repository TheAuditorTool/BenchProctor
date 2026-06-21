# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest07014(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
