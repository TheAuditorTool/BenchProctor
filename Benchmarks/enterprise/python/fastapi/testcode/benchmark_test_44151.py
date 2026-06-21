# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
from types import SimpleNamespace


async def BenchmarkTest44151(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    ns = SimpleNamespace(payload=file_value)
    data = getattr(ns, 'payload')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
