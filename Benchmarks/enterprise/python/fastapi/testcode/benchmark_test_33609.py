# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest33609(request: Request):
    host_value = request.headers.get('host', '')
    data = ensure_str(host_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
