# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest27430(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return {"updated": True}
