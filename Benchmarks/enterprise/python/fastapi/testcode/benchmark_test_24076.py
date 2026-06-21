# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest24076(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
