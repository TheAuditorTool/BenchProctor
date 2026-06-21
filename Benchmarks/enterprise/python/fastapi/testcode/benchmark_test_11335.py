# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest11335(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    Fernet(file_value.encode() if isinstance(file_value, str) else file_value).encrypt(b'data')
    return {"updated": True}
