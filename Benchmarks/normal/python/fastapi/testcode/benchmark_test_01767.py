# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest01767(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
