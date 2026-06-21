# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest01401(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ctx = RequestContext(upload_name)
    data = ctx.payload
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
