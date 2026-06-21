# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
from urllib.parse import unquote
import time


async def BenchmarkTest34122(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    store_cred = os.environ.get('APP_SECRET', '')
    key_expires_at = 4102444800
    active_key = store_cred if key_expires_at > int(time.time()) else os.environ['DATA_ENC_KEY_CURRENT']
    Fernet(active_key.encode()).encrypt(str(data).encode())
    return {"updated": True}
