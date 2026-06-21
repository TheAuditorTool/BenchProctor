# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest61127(request: Request):
    secret_value = 'config_secret_test_abc123'
    Fernet(secret_value.encode() if isinstance(secret_value, str) else secret_value).encrypt(b'data')
    return {"updated": True}
