# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest28386(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return {"updated": True}
