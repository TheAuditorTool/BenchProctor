# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest43912(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return {"updated": True}
