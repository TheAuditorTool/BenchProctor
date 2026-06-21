# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest72885(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(prop_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
