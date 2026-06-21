# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest62959(request: Request):
    secret_value = 'config_secret_test_abc123'
    reader = make_reader(secret_value)
    data = reader()
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
