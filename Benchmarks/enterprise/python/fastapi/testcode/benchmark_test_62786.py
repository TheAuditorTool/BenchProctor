# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest62786(request: Request):
    host_value = request.headers.get('host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
