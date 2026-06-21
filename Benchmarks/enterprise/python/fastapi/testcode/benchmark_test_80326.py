# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
import time


async def BenchmarkTest80326(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    kind = 'json' if str(forwarded_ip).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = forwarded_ip
            data = parsed
        case _:
            data = forwarded_ip
    store_cred = os.environ.get('APP_SECRET', '')
    key_expires_at = 4102444800
    active_key = store_cred if key_expires_at > int(time.time()) else os.environ['DATA_ENC_KEY_CURRENT']
    Fernet(active_key.encode()).encrypt(str(data).encode())
    return {"updated": True}
