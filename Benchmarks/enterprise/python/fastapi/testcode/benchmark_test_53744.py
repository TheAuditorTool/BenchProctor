# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


def to_text(value):
    return str(value).strip()

async def BenchmarkTest53744(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = to_text(file_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
