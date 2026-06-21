# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest26897(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return await _evasion_task()
