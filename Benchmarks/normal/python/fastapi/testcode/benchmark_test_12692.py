# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import keyring


async def BenchmarkTest12692(request: Request):
    secret_value = 'feature_flag_value'
    data, _sep, _rest = str(secret_value).partition('\x00')
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
