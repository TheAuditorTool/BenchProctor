# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest01920(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
