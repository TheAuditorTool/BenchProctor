# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest14624(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    def _primary():
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
