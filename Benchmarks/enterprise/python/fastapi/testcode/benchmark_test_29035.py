# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest29035(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(file_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
