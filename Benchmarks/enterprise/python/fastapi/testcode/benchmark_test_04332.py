# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest04332(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return {"updated": True}
