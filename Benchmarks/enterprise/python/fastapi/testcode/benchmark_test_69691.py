# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest69691(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    if secret_value:
        data = secret_value
    else:
        data = ''
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
