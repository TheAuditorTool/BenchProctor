# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest40640(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
