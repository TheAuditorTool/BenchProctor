# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest30131(request: Request):
    secret_value = 'config_secret_test_abc123'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    auth_check('user', data)
    return {"updated": True}
