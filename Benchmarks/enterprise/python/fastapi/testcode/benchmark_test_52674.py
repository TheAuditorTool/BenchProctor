# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest52674(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    parts = []
    for token in str(file_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
