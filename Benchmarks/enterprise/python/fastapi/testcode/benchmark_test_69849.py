# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest69849(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    ctx = RequestContext(secret_value)
    data = ctx.payload
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
