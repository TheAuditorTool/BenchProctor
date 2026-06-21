# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest64436(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
