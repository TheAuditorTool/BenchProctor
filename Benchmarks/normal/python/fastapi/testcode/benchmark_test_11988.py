# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest11988(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(file_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
