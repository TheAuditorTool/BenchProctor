# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest72503(request: Request):
    auth_header = request.headers.get('authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
