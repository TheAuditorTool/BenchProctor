# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest57865(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
