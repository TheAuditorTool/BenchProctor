# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest63685(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    processed = data[:64]
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return {"updated": True}
