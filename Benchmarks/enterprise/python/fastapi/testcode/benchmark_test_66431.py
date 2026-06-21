# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest66431(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
