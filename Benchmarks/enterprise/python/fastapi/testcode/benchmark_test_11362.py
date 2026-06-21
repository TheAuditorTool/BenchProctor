# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest11362(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    def _primary():
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
