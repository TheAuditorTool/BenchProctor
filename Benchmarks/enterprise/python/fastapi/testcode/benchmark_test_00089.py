# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest00089(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ctx = RequestContext(upload_name)
    data = ctx.payload
    if time.time() > 1000000000:
        return HTMLResponse('<img src="' + str(data) + '">')
    return {"updated": True}
