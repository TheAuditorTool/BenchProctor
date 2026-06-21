# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest34587(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ensure_str(auth_header)
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return {"updated": True}
