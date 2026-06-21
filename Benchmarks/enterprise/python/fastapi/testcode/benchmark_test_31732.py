# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def relay_value(value):
    return value

async def BenchmarkTest31732(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = relay_value(raw_body)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return {"updated": True}
