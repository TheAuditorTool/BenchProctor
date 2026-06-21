# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from urllib.parse import unquote
import os


async def BenchmarkTest81053(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return {"updated": True}
