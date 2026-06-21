# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import keyring


def ensure_str(value):
    return str(value)

async def BenchmarkTest17445(request: Request):
    secret_value = 'app_display_name'
    data = ensure_str(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
