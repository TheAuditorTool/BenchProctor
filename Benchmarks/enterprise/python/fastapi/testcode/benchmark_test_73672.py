# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest73672(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ctx = RequestContext(upload_name)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return {"updated": True}
