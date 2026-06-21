# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest79036(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = file_value if file_value else 'default'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
