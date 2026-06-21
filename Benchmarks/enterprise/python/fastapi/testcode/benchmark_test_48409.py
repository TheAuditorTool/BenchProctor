# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest48409(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    kind = 'json' if str(config_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = config_value
            data = parsed
        case _:
            data = config_value
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
