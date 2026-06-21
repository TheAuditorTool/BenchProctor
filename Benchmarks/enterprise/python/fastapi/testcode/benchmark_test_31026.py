# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest31026(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ctx = RequestContext(dotenv_value)
    data = ctx.payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
