# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest36283(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return {"updated": True}
