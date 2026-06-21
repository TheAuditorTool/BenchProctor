# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest73636(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ctx = RequestContext(upload_name)
    data = ctx.payload
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return {"updated": True}
