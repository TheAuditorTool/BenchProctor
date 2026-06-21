# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest01171(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = (lambda v: v.strip())(file_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
