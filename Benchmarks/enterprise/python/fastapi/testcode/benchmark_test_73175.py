# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest73175(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    parts = []
    for token in str(prop_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
