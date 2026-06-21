# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


request_state: dict[str, str] = {}

async def BenchmarkTest07967(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    request_state['last_input'] = config_value
    data = request_state['last_input']
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
