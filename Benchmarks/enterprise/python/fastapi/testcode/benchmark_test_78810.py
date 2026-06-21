# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest78810(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return {"updated": True}
