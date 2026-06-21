# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest22748(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    processed = data[:64]
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return {"updated": True}
