# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest39391(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    processed = data[:64]
    globals()['counter'] = int(processed)
    return {"updated": True}
