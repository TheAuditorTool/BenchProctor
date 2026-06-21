# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest45220(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ctx = RequestContext(upload_name)
    data = ctx.payload
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
