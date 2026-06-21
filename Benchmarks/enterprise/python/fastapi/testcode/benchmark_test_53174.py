# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


def to_text(value):
    return str(value).strip()

async def BenchmarkTest53174(request: Request):
    secret_value = 'config_secret_test_abc123'
    data = to_text(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
