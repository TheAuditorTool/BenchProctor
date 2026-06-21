# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest48836(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
