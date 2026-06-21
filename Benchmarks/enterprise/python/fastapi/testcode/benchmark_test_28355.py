# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
import time


async def BenchmarkTest28355(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '{}'.format(xml_value)
    store_cred = os.environ.get('APP_SECRET', '')
    key_expires_at = 4102444800
    active_key = store_cred if key_expires_at > int(time.time()) else os.environ['DATA_ENC_KEY_CURRENT']
    Fernet(active_key.encode()).encrypt(str(data).encode())
    return {"updated": True}
