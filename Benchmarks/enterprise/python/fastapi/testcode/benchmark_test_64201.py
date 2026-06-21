# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest64201(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    if file_value:
        data = file_value
    else:
        data = ''
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
