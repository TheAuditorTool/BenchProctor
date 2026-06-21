# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest14330(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return {"updated": True}
