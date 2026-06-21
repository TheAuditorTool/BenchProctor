# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest44478(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
