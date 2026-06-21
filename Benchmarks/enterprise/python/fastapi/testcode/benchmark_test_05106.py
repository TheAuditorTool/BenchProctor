# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import keyring


def normalise_input(value):
    return value.strip()

async def BenchmarkTest05106(request: Request):
    secret_value = 'feature_flag_value'
    data = normalise_input(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
