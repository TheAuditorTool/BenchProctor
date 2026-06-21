# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest19616(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '{}'.format(multipart_value)
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return {"updated": True}
