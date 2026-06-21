# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest48191(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = default_blank(upload_name)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return {"updated": True}
