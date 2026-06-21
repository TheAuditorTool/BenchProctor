# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest07100(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(config_value).encode())
    return {"updated": True}
