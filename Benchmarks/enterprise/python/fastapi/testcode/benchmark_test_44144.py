# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest44144(request: Request):
    secret_value = 'config_secret_test_abc123'
    data = secret_value if secret_value else 'default'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
