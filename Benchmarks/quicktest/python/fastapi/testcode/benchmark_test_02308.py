# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def relay_value(value):
    return value

async def BenchmarkTest02308(request: Request):
    secret_value = 'feature_flag_value'
    data = relay_value(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
