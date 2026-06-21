# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest02675(request: Request):
    referer_value = request.headers.get('referer', '')
    data = default_blank(referer_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return {"updated": True}
