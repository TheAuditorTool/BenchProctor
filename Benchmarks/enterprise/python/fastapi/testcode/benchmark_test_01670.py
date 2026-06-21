# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest01670(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = to_text(upload_name)
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return {"updated": True}
