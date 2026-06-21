# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest72305(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    if request.session.get('user') is None:
        return JSONResponse({'error': 'no session'}, status_code=401)
    request.session['user'] = str(data)
    return {"updated": True}
