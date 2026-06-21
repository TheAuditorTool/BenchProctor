# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest28937(request: Request):
    secret_value = 'app_display_name'
    reader = make_reader(secret_value)
    data = reader()
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
