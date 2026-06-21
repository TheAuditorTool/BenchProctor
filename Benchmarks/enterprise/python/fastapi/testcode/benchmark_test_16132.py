# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest16132(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    Fernet(prop_value.encode() if isinstance(prop_value, str) else prop_value).encrypt(b'data')
    return {"updated": True}
