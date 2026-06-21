# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import base64


async def BenchmarkTest02571(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = base64.b64decode(file_value).decode('utf-8', 'ignore')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
