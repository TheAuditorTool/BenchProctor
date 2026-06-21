# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest68537(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return {"updated": True}
