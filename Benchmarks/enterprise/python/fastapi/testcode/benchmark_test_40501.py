# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest40501(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    def _primary():
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
