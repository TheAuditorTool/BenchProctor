# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest67500(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    ctx = RequestContext(secret_value)
    data = ctx.payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
