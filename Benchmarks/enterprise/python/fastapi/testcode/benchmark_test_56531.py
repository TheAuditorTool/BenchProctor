# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest56531(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return {"updated": True}
