# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import keyring


def relay_value(value):
    return value

async def BenchmarkTest46528(request: Request):
    secret_value = 'default_config_label'
    data = relay_value(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
