# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest43999(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return {"updated": True}
