# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest29065(request: Request):
    path_value = request.path_params.get('id', '')
    data = coalesce_blank(path_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return {"updated": True}
