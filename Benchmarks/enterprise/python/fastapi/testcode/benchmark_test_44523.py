# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import keyring


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest44523(request: Request):
    secret_value = 'app_display_name'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
