# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest70845(request: Request):
    secret_value = 'app_display_name'
    data = ensure_str(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
