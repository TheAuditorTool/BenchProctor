# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest23170(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    if time.time() > 1000000000:
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
