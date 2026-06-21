# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest41513(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ctx = RequestContext(upload_name)
    data = ctx.payload
    processed = data[:64]
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return {"updated": True}
