# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest73267(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = file_value.decode('utf-8', 'ignore') if isinstance(file_value, bytes) else file_value
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
