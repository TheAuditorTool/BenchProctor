# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest10326(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    if secret_value:
        data = secret_value
    else:
        data = ''
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
