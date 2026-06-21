# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest22305(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    kind = 'json' if str(secret_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = secret_value
            data = parsed
        case _:
            data = secret_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
