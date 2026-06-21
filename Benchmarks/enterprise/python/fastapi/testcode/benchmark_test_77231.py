# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import keyring
from types import SimpleNamespace


async def BenchmarkTest77231(request: Request):
    secret_value = 'feature_flag_value'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
